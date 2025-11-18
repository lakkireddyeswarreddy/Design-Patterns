

"""
Flyweight pattern is used to minimize the memory usage by using the shared data for common objects.
It is used when you have large number of similar objects, like trees in gaming, bullets in gaming.

"""
from bullet import Bullet
from bullet_factory import BulletFactory

if __name__ == "__main__":
    
    bullets = list()
    
    bullets.append(Bullet(5,0,10,BulletFactory.get_bullet_type("pistol","gold")))
    bullets.append(Bullet(3,6,30,BulletFactory.get_bullet_type("pistol","silver")))
    bullets.append(Bullet(6,0,15,BulletFactory.get_bullet_type("pistol","gold")))
    bullets.append(Bullet(5,6,10,BulletFactory.get_bullet_type("AKM","gold")))
    bullets.append(Bullet(51,20,10,BulletFactory.get_bullet_type("shotGun","gold")))
    bullets.append(Bullet(5,0,10,BulletFactory.get_bullet_type("pistol","gold")))

    for bullet in bullets:
        bullet.fire()