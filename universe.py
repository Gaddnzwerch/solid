import gettext
import logging
import stellarobjectfactory 

if __name__ == '__main__':
	try:
		#logging.basicConfig(filename='example.log', filemode='w',level=logging.DEBUG, format="%(asctime)s %(levelname)s %(filename)s %(funcName)s : %(message)s")
		logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s : %(message)s")
		de = gettext.translation('solid', localedir='locale', fallback=True, languages=['de'])
		de.install()
		l_stellar_system = stellarobjectfactory.StellarSystemFactory.create()
	except Exception as e:
		logging.critical(e)
		raise e 