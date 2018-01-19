
import mled, animations

matrix = mled.driver(13, 14)


matrix.clear()
matrix.setIntensity(7)

ani = mled.animation(matrix)

ani.loop(0, 33, animations.ani_heart_pulse + animations.ani_pacman_pulse + animations.ani_ghost_pulse)
