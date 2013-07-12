# encoding: utf-8

RS = "053150000000"

# Stadtname für Logfile
CITY = 'koeln'

# Currently, only "mongodb" is supported
DB_TYPE = 'mongodb'

# Name of the MongoDB database
DB_NAME = 'scrapearis'

# Use "localhost" if MongoDB is running on the same machine
DB_HOST = 'localhost'

# MongoDB default port is 27017
DB_PORT = 27017

# SessionNet base url, should include trailing slash
BASE_URL = 'http://ratsinformation.stadt-koeln.de/'

# Name to identify your crawler to the server
USER_AGENT_NAME = 'scrape-a-ris/0.1'

# Number of seconds to wait between requests. Increase this
# if the systems behaves unstable (seconds)
WAIT_TIME = 0.2

# Log level (DEBUG, INFO, WARNING, ERROR or CRITICAL)
LOG_LEVEL = 'INFO'
# File to log to
LOG_BASE_DIR = '/var/log/ris-scraper/'

##### Page URL masks

URLS = {
    'ASP': {
        # Month calender page
        'CALENDAR_MONTH_PARSE_PATTERN': 'si0040.asp?__cjahr={year:d}&__cmonat={month:d}',
        'CALENDAR_MONTH_PRINT_PATTERN': BASE_URL + 'si0040.asp?__cjahr=%d&__cmonat=%d',

        # Session detail page
        'SESSION_DETAIL_PARSE_PATTERN': 'to0040.asp?__ksinr={session_id:d}',
        'SESSION_DETAIL_PRINT_PATTERN': BASE_URL + 'to0040.asp?__ksinr=%d',

        # Committee detail page
        'COMMITTEE_DETAIL_PARSE_PATTERN': 'kp0040.asp?__kgrnr={committee_id:d}',
        'COMMITTEE_DETAIL_PRINT_PATTERN': BASE_URL + 'kp0040.asp?__kgrnr=%d',

        # Submission detail page
        'SUBMISSION_DETAIL_PARSE_PATTERN': 'vo0050.asp?__kvonr={submission_id:d}',
        'SUBMISSION_DETAIL_PRINT_PATTERN': BASE_URL + 'vo0050.asp?__kvonr=%d',

        # Attachment file download target file name(s)
        'ATTACHMENT_DOWNLOAD_TARGET': ['ydocstart.asp', 'getfile.asp']
    },
    'PHP': {
        # Month calender page
        'CALENDAR_MONTH_PARSE_PATTERN': 'si0040.php?__cjahr={year:d}&__cmonat={month:d}',
        'CALENDAR_MONTH_PRINT_PATTERN': BASE_URL + 'si0040.php?__cjahr=%d&__cmonat=%d',

        # Session detail page
        'SESSION_DETAIL_PARSE_PATTERN': 'to0040.php?__ksinr={session_id:d}',
        'SESSION_DETAIL_PRINT_PATTERN': BASE_URL + 'to0040.php?__ksinr=%d',

        # Committee detail page
        'COMMITTEE_DETAIL_PARSE_PATTERN': 'kp0040.php?__kgrnr={committee_id:d}',
        'COMMITTEE_DETAIL_PRINT_PATTERN': BASE_URL + 'kp0040.php?__kgrnr=%d',

        # Submission detail page
        'SUBMISSION_DETAIL_PARSE_PATTERN': 'vo0050.php?__kvonr={submission_id:d}',
        'SUBMISSION_DETAIL_PRINT_PATTERN': BASE_URL + 'vo0050.php?__kvonr=%d',

        # Attachment file download target file name
        'ATTACHMENT_DOWNLOAD_TARGET': ['ydocstart.php', 'getfile.php']
    }
}

##### XPATH strings to find elements within pages


XPATH = {
    'ASP': {
        # session title within the session details page
        'SESSION_DETAIL_TITLE': '//h1',

        # table fields with session identifier, comittee name and more details
        'SESSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

        # link to committe within the session details page
        #'SESSION_DETAIL_COMMITTEE_LINK': '//li[@class="smcmenucontext_fct_gremium"]/a',
        'SESSION_DETAIL_COMMITTEE_LINK': '//a[@class="smccontextmenulink"]',

        # table rows containing agendaitems on session detail page
        #'SESSION_DETAIL_AGENDA_ROWS': '//*[@id="smc_page_to0040_contenttable1"]/tbody/tr',
        'SESSION_DETAIL_AGENDA_ROWS': '//*[@class="smccontenttable smc_page_to0040_contenttable"]/tbody/tr',

        # link to submission in agenda item row on session detail page
        'SESSION_DETAIL_AGENDA_ROWS_SUBMISSION_LINK': 'td/a',

        # table with session-related attachment downloads on session detail page
        'SESSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]/table',

        # distinct class of the box/table containing session-related attachment downloads
        'SESSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocboxright',

        # Same as above, for the submission detail page (Vorlagen-Detailseite)
        'SUBMISSION_DETAIL_TITLE': '//h1',

        'SUBMISSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

        # "Beratungsfolge" table rows
        'SUBMISSION_DETAIL_AGENDA_ROWS': '//*[@id="smc_page_vo0050_contenttable1"]/tbody/tr',

        'SUBMISSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]/table',

        'SUBMISSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocboxright',
    },
    'PHP': {
        # session title within the session details page
        'SESSION_DETAIL_TITLE': '//h1',

        # table fields with session identifier, comittee name and more details
        'SESSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

        # link to committe within the session details page
        #'SESSION_DETAIL_COMMITTEE_LINK': '//li[@class="smcmenucontext_fct_gremium"]/a',
        'SESSION_DETAIL_COMMITTEE_LINK': '//a[@class="smccontextmenulink"]',
        
        # table rows containing agendaitems on session detail page
        'SESSION_DETAIL_AGENDA_ROWS': '//*[@class="smccontenttable smc_page_to0040_contenttable"]/tbody/tr',

        # link to submission in agenda item row on session detail page
        'SESSION_DETAIL_AGENDA_ROWS_SUBMISSION_LINK': './/a',

        # table with session-related attachment downloads on session detail page
        'SESSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]//table',

        # distinct class of the box/table containing session-related attachment downloads
        'SESSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocbox',

        # Same as above, for the submission detail page (Vorlagen-Detailseite)
        'SUBMISSION_DETAIL_TITLE': '//h1',
        'SUBMISSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

        # "Beratungsfolge" table rows
        'SUBMISSION_DETAIL_AGENDA_ROWS': '//*[@class="smccontenttable smc_page_vo0050_contenttable"]/tbody/tr',

        'SUBMISSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]//table',

        'SUBMISSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocbox'
    }
}

###### Result normalization mapping

RESULT_STRINGS = {
    
}

FILE_EXTENSIONS = {
    'application/pdf': 'pdf',
    'image/tiff': 'tif',
    'image/jpeg': 'jpg',
    'application/vnd.ms-powerpoint': 'pptx',
    'application/msword': 'doc',
    'application/zip': 'zip'
}