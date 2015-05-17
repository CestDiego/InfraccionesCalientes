import urllib
import os.path

oauth_api_key = "7b1aec2e2f430a4a357d6317c07dda2a0e6999fa"
guid_array = [
    "CONTR-2015",
    "PORCE-EFECT-ARBIT-POR-ZONAS",
    "PREDI-DE-VALUO-2011",
    "PREDI-DE-VALUO-2012",
    "PREDI-DE-VALUO-2013",
    "PREDI-DE-VALUO-2014",
    "PREDI-DE-VALUO-2015",
    "PROME-DE-VALUO",
    "CONTR-2014-93688",
    "CONTR-2014-93688",
    "PROCE-DE-CONTR",
    "ORDEN-DE-COMPR-Y-SERVI",
    # Comercio
    "COMER-EN-MIRAF",
    "COMER",
    "FARMA-Y-BOTIC-29293",
    "CENTR-EDUCA",
    "GIMNA-18402",
    "TIPO-CENTR-SALUD",
    "CENTR-DE-SALUD-36680",
    "VETER",
    # Educacion y cultura
    "INSTI-Y-ASOCI-CULTU",
    "LIBRE-Y-VENTA-DE-29117",
    "EDUCA",
    "MUSEO-TEATR-Y-CINES-CULTU",
    # Edificiios
    "RESOL-DE-EDIFI",
    #  Fiscal
    "FUNCI-Y-SANID-55078",
    "RUIDO",
    "OTROS",
    "ESTAD-DE-INFRA",
    "FISCA-TRIBU",
    "RESOL-DE-SANCI-IMPUE",
    # OBRAS
    "GESTO",
    "LUMIN",
    "MANTE-INTEG-DE-VIAS",
    "MANTE-PARCI-DE-VIAS",
    "RAMPA",
    "SENAL",
    "PROYE-POR-MANTE",
    # Presupuesto


    "INFRA-31368",
]

url = "http://miraflores.cloudapi.junar.com/datastreams/invoke/{0:}?auth_key={1:}&output=json_array"
for guid in guid_array:

    le_filename = guid + ".json"
    if os.path.isfile(le_filename):
        print "Skipped ", le_filename
        continue

    le_url = url.format(guid, oauth_api_key)

    requests = urllib.urlopen(le_url)

    textResponse = requests.read()

    jsonResponse = json.loads(textResponse)

    try:
        data = jsonResponse['result']
    except:
        print guid
        print le_url
        print jsonResponse
        raise

    keys = []

    dictData = []

    for i, row in enumerate(data):
        if i == 0:
            keys = [item.replace('-', '_') for item in row]
        else:
            dictData.append(dict(zip(keys, row)))

    with open(le_filename, 'w') as outfile:
        print "Wrote ", le_filename
        json.dump(dictData, outfile, indent=2)
