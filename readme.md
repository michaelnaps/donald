### **Path-following robot:** Daffy

This repository serves as the testing grounds for functions and classes that will be used for the development of my personal robot, Daffy.

State/Model Selection:
$$
    x = \left[ \begin{matrix}
        x \\ y \\ \theta
    \end{matrix} \right]
$$
$$
    \dot{x} = \left[ \begin{matrix}
        \dot x_1 \\ \dot x_2 \\ \dot x_3
    \end{matrix} \right]
    = \left[ \begin{matrix}
        \dot x \\ \dot y \\ \dot \theta
    \end{matrix} \right]
    = \left[ \begin{matrix}
        \textrm{cos} (x_3) (u_1 + u_2) \\
        \textrm{sin} (x_3) (u_1 + u_2) \\
        \frac{1}{R} (u_1 + u_2)
    \end{matrix} \right]
$$
