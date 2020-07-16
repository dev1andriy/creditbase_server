from common.urls import base_parties as base_parties_urls
from common.urls import related_parties as related_parties_urls
from common.urls import business_analysis as business_analysis_urls
from common.urls import documents as documents_urls
from common.urls import communications as communications_urls
from common.urls import credit_applications as credit_applications_urls
from common.urls import arrangements as arrangements_urls
from common.urls import other as other_urls
from common.urls import search as search_urls

urls = []

urls += base_parties_urls.urlpatterns
urls += related_parties_urls.urlpatterns
urls += business_analysis_urls.urlpatterns
urls += documents_urls.urlpatterns
urls += communications_urls.urlpatterns
urls += other_urls.urlpatterns
urls += credit_applications_urls.urlpatterns
urls += arrangements_urls.urlpatterns
urls += search_urls.urlpatterns
