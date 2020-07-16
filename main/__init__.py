from django.db import connections, router, transaction

UPSERT_QUERY = """
    INSERT INTO creditbase_sequence ("InsertDate", "LastUpdatedDate", "SequenceId", "Description", "TabelId", "TableName", "TableFilter", "CurrentValue", "IncrementValue", "MinimumValue", "InsertedBy", "LastUpdatedBy")
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ("SequenceId")
  DO UPDATE SET "CurrentValue" = creditbase_sequence."CurrentValue" + creditbase_sequence."IncrementValue"
      RETURNING "CurrentValue"
"""


def get_next_value(insert_data=None, last_update_date=None, sequence_id=1, description=None, table_name='default', table_filter=None, initial_value=1, increment_value=1, minimum_value=1, inserted_by=None, last_updated_by=None, reset_value=None, *, nowait=False, using=None):
    from common.models.base_parties import Sequence
    if using is None:
        using = router.db_for_write(Sequence)

    connection = connections[using]

    if (getattr(connection, 'pg_version', 0) >= 90500
            and reset_value is None and not nowait):

        # PostgreSQL ≥ 9.5 supports "upsert".

        with connection.cursor() as cursor:
            cursor.execute(UPSERT_QUERY,
                           [insert_data, last_update_date, sequence_id, description, 1, table_name, table_filter, initial_value, increment_value, minimum_value, inserted_by, last_updated_by])
            last, = cursor.fetchone()
        return last

    else:

        # Other databases require making more database queries.

        with transaction.atomic(using=using, savepoint=False):
            sequence, created = (
                Sequence.objects.select_for_update(nowait=nowait).get_or_create(name=table_name,
                                                                                defaults={'last': initial_value})
            )

            if not created:
                sequence.CurrentValue += 1
                if reset_value is not None and sequence.CurrentValue >= reset_value:
                    sequence.CurrentValue = initial_value
                sequence.save()

            return sequence.CurrentValue


''' 
def get_next_value(sequence_name='default', initial_value=1, reset_value=None, *, nowait=False, using=None):
    from .credit_base_models import Sequence
    if using is None:
        using = router.db_for_write(Sequence)

    connection = connections[using]

    if (getattr(connection, 'pg_version', 0) >= 90500
            and reset_value is None and not nowait):

        # PostgreSQL ≥ 9.5 supports "upsert".

        with connection.cursor() as cursor:
            cursor.execute(UPSERT_QUERY, [None, None, initial_value, initial_value, 1, sequence_name, None, 1, 10, 1, None, None])
            last, = cursor.fetchone()
        return last

    else:

        # Other databases require making more database queries.

        with transaction.atomic(using=using, savepoint=False):
            sequence, created = (
                Sequence.objects.select_for_update(nowait=nowait).get_or_create(name=sequence_name,
                                                                                defaults={'last': initial_value})
            )

            if not created:
                sequence.CurrentValue += 1
                if reset_value is not None and sequence.CurrentValue >= reset_value:
                    sequence.CurrentValue = initial_value
                sequence.save()

            return sequence.CurrentValue 
'''
