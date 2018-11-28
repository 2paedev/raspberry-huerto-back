class AemetConfig():
    BASE_URL = 'https://opendata.aemet.es/opendata/api'

    AEMET_API_INFO = {
        'SAN_VICENTE_RASPEIG': {
            'ID': 'id03122',
            'PROVINCIA_CODE': '03',
            'MUNICIPIO_CODE': '122',
        },
        'COMUNIDAD_VALENCIANA_AREA_ID': '77',
        'API_KEY':
        'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIycGFlZGV2QGdtYWlsLmNvbSIsImp0aSI6IjJkZjA2NjdmLWYyNTktNDY5OC1iNzQxLTliMGZkYzQ4NTlmMSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTM5NjIzODg5LCJ1c2VySWQiOiIyZGYwNjY3Zi1mMjU5LTQ2OTgtYjc0MS05YjBmZGM0ODU5ZjEiLCJyb2xlIjoiIn0.kUqNLiLml65yhTw_71tSUaE6kClYkJqJ6SYDVW7_Jv8',
    }

    AEMET_API = {
        'MASTER': {
            'SAN_VICENTE_RASPEIG': BASE_URL + '/maestro/municipio/' + AEMET_API_INFO['SAN_VICENTE_RASPEIG']['ID'],
        },
        'PREDICTION': {
            'DAILY': BASE_URL + '/prediccion/especifica/municipio/diaria/' + AEMET_API_INFO['SAN_VICENTE_RASPEIG']['PROVINCIA_CODE'] + AEMET_API_INFO['SAN_VICENTE_RASPEIG']['MUNICIPIO_CODE']
        }
    }
