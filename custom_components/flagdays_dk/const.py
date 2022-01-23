ATTRIBUTION = 'Created by J-Lindvig'
CONF_CLIENT = 'client'
CONF_PLATFORM = 'sensor'
DOMAIN = 'flagdays_dk'
EVENT_DATE_FORMAT = '%d-%m-%Y %H:%M'
FLAGS = {
	'grønland': 'Erfalasorput',
	'færø': 'Merkið'
}
FLAGDAY_URL = 'https://www.justitsministeriet.dk/temaer/flagning/flagdage/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}
HALF_MAST_DAYS = ['besættelsesdagen', 'langfredag']
HALF_MAST_ALL_DAY_STR = 'hele dagen'
ICON = 'mdi:flag'
MONTHS_DK = ['januar', 'februar', 'marts', 'april', 'maj', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december']
SUN_URL = 'https://api.sunrise-sunset.org/json'
UPDATE_INTERVAL = 60
UTC_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

CREDITS = [{'organization': 'Justitsministeriet', 'site': FLAGDAY_URL}, {'organization': 'Sunrise-Sunset', 'site': 'https://sunrise-sunset.org/api'}]