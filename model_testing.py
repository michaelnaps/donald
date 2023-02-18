# script for model equation testing
import sys
sys.path.insert(0, '/home/michaelnaps/prog/ode');

import numpy as np
import ode

import matplotlib.pyplot as plt
import matplotlib.patches as patch
import matplotlib.path as path


# hyper parameter(s)
pi = np.pi;
Nx = 3;
Nu = 2;
R = 1/2;  # robot-body radius
dt = 0.01;


class Parameters:
    def __init__(self, x0,
                 fig=None, axs=None,
                 buffer_length=10, pause=1e-3,
                 color='k'):
        if axs is None and fig is None:
            self.fig, self.axs = plt.subplots();
        else:
            self.fig = fig;
            self.axs = axs;

        self.axs.set_xlim(-2,2);
        self.axs.set_ylim(-2,2);
        self.axs.axis('equal');
        self.axs.grid();
        self.fig.tight_layout();

        # initialize buffer (trail)
        self.color = color;
        self.width = 0.05;
        self.length = R/2;

        self.buffer = np.kron( np.ones( (buffer_length, 1) ), x0[:2].reshape(1,2));
        self.trail_patch = patch.PathPatch(path.Path(self.buffer), color=self.color);

        dx1 = self.length*np.cos(x0[2]);
        dx2 = self.length*np.sin(x0[2]);
        self.orientation = patch.Arrow(x0[0], x0[1], dx1, dx2,
                                       width=self.width, color=self.color);

        self.axs.add_patch(self.trail_patch);
        self.axs.add_patch(self.orientation);

        self.pause = pause;

    def update(self, t, x):
        self.trail_patch.remove();
        self.orientation.remove();

        self.buffer[:-1] = self.buffer[1:];
        self.buffer[-1] = x[:2];

        self.trail_patch = patch.PathPatch(path.Path(self.buffer), fill=0);

        dx1 = self.length*np.cos(x[2]);
        dx2 = self.length*np.sin(x[2]);
        self.orientation = patch.Arrow(x[0], x[1], dx1, dx2,
                                       width=self.width, color=self.color);

        self.axs.add_patch(self.trail_patch);
        self.axs.add_patch(self.orientation);

        plt.show(block=0);
        plt.pause(self.pause);

        return self;

def modelFunc(x, u, _):
    dx = np.array( [
        [np.cos(x[2])*(u[0] + u[1])],
        [np.sin(x[2])*(u[0] + u[1])],
        [1/R*(u[0] - u[1])]
    ] );
    return dx;

def callbackFunc(T, x, u, mvar):
    return mvar.params.update(T, x);


if __name__ == "__main__":
    # initialize states
    x0 = np.array( [[0],[0],[pi/2]] );
    u0 = np.array( [[0],[10]] );

    # create model class variable
    model_type = 'continuous';
    params = Parameters(x0, buffer_length=10);
    daffy = ode.Model(modelFunc, model_type,
                      x0=x0, Nu=Nu, dt=dt, params=params);

    # simulate model
    sim_time = 10;
    daffy.simulate(sim_time, x0, u0=u0, callback=callbackFunc);
