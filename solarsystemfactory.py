import solarsystem
import sun
import planet

class SolarSystemFactory():
    
    def create_sol(self):
        m_solarsystem = solarsystem.SolarSystem(sun.Sun()) 
        m_solarsystem.add_planet(planet.PlanetFactory.create_mercury(), 5.7909e10) 
        m_solarsystem.add_planet(planet.PlanetFactory.create_venus(), 1.0816e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_earth(), 1.496e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_mars(), 2.22799e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_jupiter(), 7.7836e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_saturn(), 14.335e11)
        return m_solarsystem
