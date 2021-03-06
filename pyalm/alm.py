import sys
import requests
import csv
import pandas as pd

def alm(doi = None, pmid = None, pmcid = None, mdid = None, url = 'http://alm.plos.org/api/v3/articles', info = "totals", 
		months = None, days = None, year = None, source = None, key = None):
	'''
	Get summary altmetrics from PLOS ALM or another provider that's used the PLOS ALM app

	You need to get an API key before you use this function. You can supply your key using the key 
	argument in the function call or put it in a csv file called pkeys.csv using the structure

	keyname,key
	plosalmkey,WQcDSXml2VSWx3P
	
	E.g. calls
	pyalm.alm(doi='10.1371/journal.pmed.1001361', key='WQcDSXml2VSWx3P')
	pyalm.alm(doi=['10.1371/journal.pone.0001543','10.1371/journal.pone.0040117'], key='WQcDSXml2VSWx3P')
	'''	
	# Convert info parameter
	# if(!info %in% c("summary","totals","history","detail")):
	# 	stop("info must be one of summary, totals, history, or detail")
	# else:
	# 	pass

	# remove any DOIs of images
	# if(doi.__class__.__name__ == 'NoneType'):
	# 	doi = doi[!grepl("image", doi)]

	# create id object, check to make sure only one of doi, pmid, pmcid, or mdid supplied 
	id = {'doi':doi, 'pmid':pmid, 'pmcid':pmcid, 'mendeley':mdid}
	id2 = delNone(id)
	# if(len(id) > 1):
	# 	print("Only supply one of: doi, pmid, pmcid, mdid")
	# else: 
	# 	id2 = delNone(id)

	if(id2.values()[0][0].__len__() == 1):
		id2 = id2.values()[0]
	else:
		id2 = ','.join(id2.values()[0])

	# get api key
	apikey = getkey(key)
	
	if(source.__class__.__name__ == 'NoneType'):
		source2 = None
	else:
		source2 = ','.join(source)

	if(apikey == 'Sorry, you need an API key'):
		return apikey
	else:
		payload = {'api_key': apikey, 'info': info, 'months': months, 'days': days, 'year': year, 'source': source2, 'ids': id2}
		out = requests.get(url, params = payload)
		out2 = out.json()
		if(len(out2) == 1):
			stuff = out2[0]['sources']
			stuff2 = makedf(stuff)
		else:
			stuff = []
			for x in out2:
				tmp = x['sources']
				stuff.append(makedf(tmp))
			stuff2 = stuff
	  	return stuff2

def almraw(doi = None, pmid = None, pmcid = None, mdid = None, url = 'http://alm.plos.org/api/v3/articles', info = "totals", 
		months = None, days = None, year = None, source = None, key = None):
	'''
	Get summary altmetrics from PLOS ALM or another provider that's used the PLOS ALM app

	You need to get an API key before you use this function. You can supply your key using the key 
	argument in the function call or put it in a csv file called pkeys.csv using the structure

	keyname,key
	plosalmkey,WQcDSXml2VSWx3P
	
	E.g. calls
	pyalm.alm(doi='10.1371/journal.pmed.1001361', key='WQcDSXml2VSWx3P')
	pyalm.alm(doi=['10.1371/journal.pone.0001543','10.1371/journal.pone.0040117'], key='WQcDSXml2VSWx3P')
	'''	
	# create id object, check to make sure only one of doi, pmid, pmcid, or mdid supplied 
	id = {'doi':doi, 'pmid':pmid, 'pmcid':pmcid, 'mendeley':mdid}
	id2 = delNone(id)
	if(len(id2.values()[0]) == 1):
		id2 = id2.values()
	else:
		id2 = ','.join(id2.values()[0])

	# get api key
	apikey = getkey(key)
	
	if(source.__class__.__name__ == 'NoneType'):
		source2 = None
	else:
		source2 = ','.join(source)

	if(apikey == 'Sorry, you need an API key'):
		return apikey
	else:
		payload = {'api_key': apikey, 'info': info, 'months': months, 'days': days, 'year': year, 'source': source2, 'ids': id2}
		out = requests.get(url, params = payload)
		out2 = out.json()
		if(len(out2) == 1):
			stuff = out2[0]['sources']
			stuff2 = stuff
		else:
			stuff = []
			for x in out2:
				tmp = x['sources']
				stuff.append(tmp)
			stuff2 = stuff
	  	return stuff2

def getkey(key = None):
	'''
	getkey recieves the input key parameter, and outputs your key if you supply it in the fxn call, or reads 
	it from your pkeys.csv file if you don't provide one.
	'''
	if(key.__class__.__name__ == 'NoneType'):
		tt = pd.DataFrame(pd.read_csv("pykeys.csv", ','))
		gg = tt.ix[0,'key']

		if(gg.__class__.__name__ == 'str'):
			return gg
		else:
			return 'Sorry, you need an API key'
	else:
		return key

def delNone(d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    # d.iteritems isn't used as you can't del or the iterator breaks.
    for key, value in d.items():
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def makedf(input):
	'''
	Make DataFrame
	'''
	outout = []
	for x in input:
		outout.append(x['metrics'])
   	outdat = pd.DataFrame.from_dict(outout)
	outdat = outdat.rename(index={0:'bloglines',1:'citeulike',2:'connotea',3:'crossref',4:'nature',5:'postgenomic',6:'pubmed',7:'scopus',8:'counter',9:'researchblogging',10:'biod',11:'pmc',12:'facebook',13:'mendeley',14:'twitter',15:'wikipedia',16:'scienceseeker',17:'relativemetric',18:'f1000',19:'figshare',20:'pmceurope',21:'pmceuropedata',22:'openedition',23:'wordpress',24:'reddit'})
	return outdat