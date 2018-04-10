import gettext
import logging
import stellarobjectfactory 
import units
import units.predefined

if __name__ == '__main__':
	try:
		units.predefined.define_units()
		assert units.unit('m').is_si()
		km = units.unit('km')				
		au = units.unit('AU')
		diameter = au(1)
		#logging.debug(km(diameter))
		#logging.basicConfig(filename='example.log', filemode='w',level=logging.DEBUG, format="%(asctime)s %(levelname)s %(filename)s %(funcName)s : %(message)s")
		logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s : %(message)s")
		de = gettext.translation('solid', localedir='locale', fallback=True, languages=['de'])
		de.install()		
		l_stellar_system = stellarobjectfactory.StellarSystemFactory.create()
	except Exception as e:
		logging.critical(e)
		raise e 