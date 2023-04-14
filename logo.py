import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import imageio
import imageio.v2 as imageio


r = 2    # radius
w = 1    # width

def circle(t):
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = 0
    return np.array([x, y, z])

# def mobius(t, s, i):
#     x = (r + s * np.cos(t/2)) * np.cos(t)
#     y = (r + s * np.cos(t/2)) * np.sin(t)
#     z = s * np.sin(t/2)
#     return np.array([x, y, z])

def mobius(t, s, i):
    x = (r + s * np.cos(t/2 + i/10)) * np.cos(t)
    y = (r + s * np.cos(t/2 + i/10)) * np.sin(t)
    z = s * np.sin(t/2 + i/10)
    return np.array([x, y, z])

colors = ['#29ABE2', '#FBB03B', '#F15A24', '#ED1E79', '#6C2583']
def gradient_colors(colors):
    num_colors = len(colors)
    custom_gradient = []
    # custom_gradient.append((0, colors[0]))
    # custom_gradient.append((0.18, colors[0]))
    # custom_gradient.append((0.40, colors[1]))
    # custom_gradient.append((0.55, colors[2]))
    # custom_gradient.append((0.8, colors[3]))
    # custom_gradient.append((1, colors[4]))

    custom_gradient.append((0, colors[4]))
    custom_gradient.append((0.2, colors[3]))
    custom_gradient.append((0.45, colors[2]))
    custom_gradient.append((0.60, colors[1]))
    custom_gradient.append((0.82, colors[0]))
    custom_gradient.append((1, colors[0]))
    
    cmap = LinearSegmentedColormap.from_list('custom', custom_gradient)
    gradient = np.linspace(0, 1, 100)
    gradient_colors = cmap(gradient)
    return gradient_colors
cmap = ListedColormap(gradient_colors(colors))
t = np.linspace(0, 2*np.pi, 100)
s = np.linspace(-w/2, w/2, 100)
T, S = np.meshgrid(t, s)
X, Y, Z = mobius(T, S, 0)
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none')
ax.set_axis_off()
filename = 'mobius_strip.png'
plt.savefig(filename, dpi=1800, bbox_inches='tight', pad_inches=0)
ax.set_axis_off()
plt.show()

# Create the frames
# set up the viewing angle
# elev_angle = 50
# azim_angle = 0
# num_frames = 90

# frames = []
# for i in range(num_frames):
#     X, Y, Z = mobius(T, S, i)
#     fig = plt.figure(facecolor='black')
#     ax = fig.add_subplot(111, projection='3d')

#     surf = ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none')
#     ax.set_axis_off()
#     filename = f'mobius_strip_{i}.png'
#     ax.view_init(elev=elev_angle, azim=azim_angle)

#     plt.savefig(filename, dpi=96, bbox_inches='tight', pad_inches=0, transparent=True)
#     # azim_angle += 360/num_frames

#     # plt.savefig(filename, dpi=1800, bbox_inches='tight', pad_inches=0)
#     frames.append(imageio.imread(filename))
#     plt.close()

# # Save the frames as a GIF
# imageio.mimsave('mobius_strip.gif', frames, fps=20, duration=0.1)