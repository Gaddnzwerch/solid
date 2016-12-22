import sun
import planet
import gettext

if __name__ == '__main__':
    de = gettext.translation('solid', localedir='locale', languages=['de'])
    de.install()
    mSun = sun.Sun() 
    print(mSun)
    m_planet = planet.Planet()
    print(m_planet)
