## Background
Hello this Liam Patel UH ID and my project is a Qualitative simulator of small particle interactions

## Requirements
-python 3.8+

-pygame

```bash
pip install pygame
```



## Forces

1. Electric Force

    Utilized Coulomb's Law F=(K*q1*q2/r)to calculate electric force between every particle in the simulation


    ```bash
    radius = math.sqrt((dx)**2 + (dy)**2)/20
    force_magnitude = (p1.charge* p2.charge)/ (radius**2)
    fx = force_magnitude *dx / radius
    fy = force_magnitude * dy/radius
    ```
2. Gravitational Force

    Utilized the over simplified equation (F=mg) to calcuate the gravitational force due to earths gravity.

    ```bash
    def force_gravity(self,p1,dt):
        Fg = p1.mass * 9.8
        ay = Fg / p1.mass
        p1.vel.y += ay * dt
    ```

3. Strong Nuclear Force

    Utilized my own algorithm to create a visually accurate force. First I made sure the force only worked at very close distances between nucleons. I also made sure to make sure the strong nuclear force overpowered any other force in the simulation, due to its strong nature.


    ```bash
    force_magnitude = (g**2) *math.exp(-radius*range_force)/range_force
        if radius < range_force:
            p1.nuke=True
            p2.nuke = True
            p1.vel *= -((radius/2)**2)
            p2.vel *= -((radius/2)**2)
        else:
            p1.nuke = False
            p2.nuke = False
    ```
