from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import (
    black,
    blue,
    purple,
    white,
    yellow
)

class ArrlRadiogram:

    defaults = {
        'padding_top': 3,
        'align': TA_LEFT
    }

    styles = {
        'default': ParagraphStyle(
            'default',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=5,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Helvetica',
            bulletFontSize=10,
            bulletIndent=0,
            textColor=blue,
            backColor=None,
            wordWrap=None,
            borderWidth=0,
            borderPadding=0,
            borderColor=None,
            borderRadius=None,
            allowWidows=1,
            allowOrphans=0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }

    data_map = {
        'ARRL_MSG_NUMBER': {'align': TA_CENTER},
        'ARRL_MSG_PRECEDENCE': {'align': TA_CENTER},
        'ARRL_MSG_HX': {'align': TA_CENTER},
        'ARRL_MSG_STATION_OF_ORIGIN': {'align': TA_CENTER},
        'ARRL_MSG_CHECK': {'align': TA_CENTER},
        'ARRL_MSG_PLACE_OF_ORIGIN': {'align': TA_CENTER},
        'ARRL_MSG_TIME': {'align': TA_CENTER},
        'ARRL_MSG_DATE': {'align': TA_CENTER},
        'ARRL_MSG_ADDRESS': {},
        'ARRL_MSG_PHONE': {},
        'ARRL_MSG_EMAIL': {},
        'ARRL_MSG_WORD_1': {},
        'ARRL_MSG_WORD_2': {},
        'ARRL_MSG_WORD_3': {},
        'ARRL_MSG_WORD_4': {},
        'ARRL_MSG_WORD_5': {},
        'ARRL_MSG_WORD_6': {},
        'ARRL_MSG_WORD_7': {},
        'ARRL_MSG_WORD_8': {},
        'ARRL_MSG_WORD_9': {},
        'ARRL_MSG_WORD_10': {},
        'ARRL_MSG_WORD_11': {},
        'ARRL_MSG_WORD_12': {},
        'ARRL_MSG_WORD_13': {},
        'ARRL_MSG_WORD_14': {},
        'ARRL_MSG_WORD_15': {},
        'ARRL_MSG_WORD_16': {},
        'ARRL_MSG_WORD_17': {},
        'ARRL_MSG_WORD_18': {},
        'ARRL_MSG_WORD_19': {},
        'ARRL_MSG_WORD_20': {},
        'ARRL_MSG_WORD_21': {},
        'ARRL_MSG_WORD_22': {},
        'ARRL_MSG_WORD_23': {},
        'ARRL_MSG_WORD_24': {},
        'ARRL_MSG_WORD_25': {},
        'ARRL_STATION_CALLSIGN': {},
        'ARRL_STATION_PHONE': {},
        'ARRL_STATION_NAME': {},
        'ARRL_STATION_EMAIL': {},
        'ARRL_STATION_STREET': {},
        'ARRL_STATION_CITY_STATE_ZIP': {},
        'ARRL_RECD_FROM': {},
        'ARRL_RECD_DATE': {},
        'ARRL_RECD_TIME': {},
        'ARRL_SENT_TO': {},
        'ARRL_SENT_DATE': {},
        'ARRL_SENT_TIME': {}
    }
