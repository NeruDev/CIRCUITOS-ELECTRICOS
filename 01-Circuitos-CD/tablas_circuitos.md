### Circuito 1: RL (Respuesta Transitoria de Descarga)

* **Parámetros en LaTeX:** $\tau = 28.89\text{ ms}$ | $L = 809\text{ mH}$ | $R_{eq} = 28\ \Omega$

| Constante | Tiempo | Corriente $i_L(t)$ | Voltaje $v_L(t)$ |
| :--- | :--- | :--- | :--- |
| $0\tau$ | 0.00 ms | 500.00 mA | -14.00 V |
| $1\tau$ | 28.89 ms | 183.94 mA | -5.15 V |
| $2\tau$ | 57.79 ms | 67.67 mA | -1.90 V |
| $3\tau$ | 86.68 ms | 24.89 mA | -0.70 V |
| $4\tau$ | 115.57 ms | 9.16 mA | -0.26 V |
| $5\tau$ | 144.46 ms | 3.37 mA | -0.09 V |

### Circuito 2: RC (Fase de Carga - Switch Cerrado)

* **Parámetros en LaTeX:** $\tau_c = 26.32\text{ ms}$ | $C = 47\ \mu\text{F}$ | $R_{\text{carga}} = 560\ \Omega$

| Constante | Tiempo | Voltaje $v_C(t)$ | Corriente $i_C(t)$ |
| :--- | :--- | :--- | :--- |
| $0\tau_c$ | 0.00 ms | 0.00 V | 16.07 mA |
| $1\tau_c$ | 26.32 ms | 5.69 V | 5.91 mA |
| $2\tau_c$ | 52.64 ms | 7.78 V | 2.18 mA |
| $3\tau_c$ | 78.96 ms | 8.55 V | 0.80 mA |
| $4\tau_c$ | 105.28 ms | 8.84 V | 0.29 mA |
| $5\tau_c$ | 131.60 ms | 8.94 V | 0.11 mA |


### Circuito 2: RC (Fase de Descarga - Switch Abierto)

* **Parámetros en LaTeX:** $\tau_d = 48.41\text{ ms}$ | $C = 47\ \mu\text{F}$ | $R_{\text{descarga}} = 1030\ \Omega$

| Constante | Tiempo | Voltaje $v_C(t)$ | Corriente $i_C(t)$ |
| :--- | :--- | :--- | :--- |
| $0\tau_d$ | 0.00 ms | 9.00 V | -8.74 mA |
| $1\tau_d$ | 48.41 ms | 3.31 V | -3.21 mA |
| $2\tau_d$ | 96.82 ms | 1.22 V | -1.18 mA |
| $3\tau_d$ | 145.23 ms | 0.45 V | -0.44 mA |
| $4\tau_d$ | 193.64 ms | 0.17 V | -0.16 mA |
| $5\tau_d$ | 242.05 ms | 0.06 V | -0.06 mA |