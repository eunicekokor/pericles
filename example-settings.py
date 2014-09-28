# You MUST fill these out for pericles.py to execute

GCAL_USERNAME="" #yourGcalUsername
GCAL_PASSWORD="" #yourGcalPassword
GCAL_ID="adicu.com_tud5etmmo5mfmuvdfb54u733i4@group.calendar.google.com"
GCAL_ID2="0rsloi9kruveudc58i5bjr468o@group.calendar.google.com"

MC_API_KEY="" #Go to settings in your Mailchimp
MC_LIST_ID= "" #Go to list settings in your Mailchimp
MC_LIST_NAME="ADI Newsletter" #Actual name of the list
MC_EMAIL="eunice@adicu.com" #can be anything
MC_FROM_NAME="Application Development Initiative"
MC_TO_NAME="ADI" #Can be anything
MC_TEMPLATE_SECTION="std_content00" #for now keep this
MC_TEMPLATE_NAME="ADI Newsletter" #name of template

# There are message templates for html and text, which vary based on the number of times available

EVENT_TEMPLATE = {}
EVENT_TEMPLATE['HTML_TITLE'] = "<h3>{title}</h3>\n"
EVENT_TEMPLATE['TEXT_TITLE'] = "{title}\n"
EVENT_TEMPLATE['HTML_START_DATE'] = "<h4>{start_date}"
EVENT_TEMPLATE['TEXT_START_DATE'] = "{start_date}"
EVENT_TEMPLATE['START_TIME'] = "{start_time}"
EVENT_TEMPLATE['END_DATE'] = "{end_date}"
EVENT_TEMPLATE['END_TIME'] = "{end_time}"
EVENT_TEMPLATE['HTML_LOC'] = " at {location}</h4>\n"
EVENT_TEMPLATE['HTML_DESC'] = "<p>{description}</p>"
EVENT_TEMPLATE['TEXT_LOC'] = " at {location}\n"
EVENT_TEMPLATE['TEXT_DESC'] = "{description}"

EVENT_HTML_TEMPLATE_WITH_ALL = (EVENT_TEMPLATE['HTML_TITLE'] + EVENT_TEMPLATE['HTML_START_DATE'] + " ," + EVENT_TEMPLATE['START_TIME'] + " &mdash; " + EVENT_TEMPLATE['END_DATE'] + ", " + EVENT_TEMPLATE['END_TIME'] + EVENT_TEMPLATE['HTML_LOC']+ EVENT_TEMPLATE['HTML_DESC'])

EVENT_HTML_TEMPLATE_DEFAULT = (EVENT_TEMPLATE['HTML_TITLE'] + EVENT_TEMPLATE['HTML_START_DATE'] + ", " +  EVENT_TEMPLATE['START_TIME'] + " &mdash; " + EVENT_TEMPLATE['END_TIME'] + EVENT_TEMPLATE['HTML_LOC'] + EVENT_TEMPLATE['HTML_DESC'])

EVENT_HTML_TEMPLATE_NO_TIMES = (EVENT_TEMPLATE['HTML_TITLE'] + EVENT_TEMPLATE['HTML_START_DATE']+ " &mdash; " + EVENT_TEMPLATE['END_DATE'] + EVENT_TEMPLATE['HTML_LOC'] + EVENT_TEMPLATE['HTML_DESC']) 

EVENT_TEXT_TEMPLATE_DEFAULT = EVENT_TEMPLATE['TEXT_TITLE'] + EVENT_TEMPLATE['TEXT_START_DATE'] + ", " + EVENT_TEMPLATE['START_TIME'] + " &mdash; " + EVENT_TEMPLATE['END_TIME'] + EVENT_TEMPLATE['TEXT_LOC'] + EVENT_TEMPLATE['TEXT_DESC']

EVENT_TEXT_TEMPLATE_NO_TIMES = (EVENT_TEMPLATE['TEXT_TITLE'] + EVENT_TEMPLATE['TEXT_START_DATE']+ " &mdash; " + EVENT_TEMPLATE['END_DATE'] + EVENT_TEMPLATE['TEXT_LOC'] + EVENT_TEMPLATE['TEXT_DESC']) 

EVENT_TEXT_TEMPLATE_WITH_ALL = (EVENT_TEMPLATE['TEXT_TITLE'] + EVENT_TEMPLATE['TEXT_START_DATE'] + ", " + EVENT_TEMPLATE['START_TIME'] +  " &mdash; " + EVENT_TEMPLATE['END_DATE'] + ", " + EVENT_TEMPLATE['END_TIME'] + EVENT_TEMPLATE['TEXT_LOC'] + EVENT_TEMPLATE['TEXT_DESC'])

SUBJECT_TEMPLATE = "ADI Newsletter %m/%d/%Y" #Solid Calendar
SUBJECT_TEMPLATE2 = "ADI Newsletter Tentative Calendar %m/%d/%Y" #Tentative Calendar. DO NOT SEND THIS ONE

DATE_FORMAT = '%A, %m/%d' #will change later
TIME_FORMAT = '%I:%M %p' #will change later

