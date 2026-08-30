# Tetris Clon

Clon del clásico juego de Tetris hecho en Python usando 'Pygame', compilado a 'WebAssembly' con 'pygbag' para poder jugarse directamente en el navegador.

[**JUGAR AHORA**](https://tetris-cloned.netlify.app/)

---

Índice

- [Características](#características)
- [Controles](#controles)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cómo correrlo en local](#cómo-correrlo-en-local)
- [Cómo funciona la demo web](#cómo-funciona-la-demo-web)
- [Despliegue en producción](#despliegue-en-producción)
- [Tecnologías](#tecnologías)

---

## Características

- Las 7 piezas clásicas del Tetris con colores distintivos
- Sistema de puntuación por líneas eliminadas
- Pieza "fantasma" (ghost piece) que muestra dónde caerá la pieza actual
- Vista previa de la siguiente pieza
- Récord persistente entre partidas
- Música de fondo
- Pantallas de inicio y de "game over" con reinicio rápido
- Jugable tanto de forma nativa (escritorio) como desde el navegador

## Controles

| Tecla | Acción |
|---|---|
| `←` / `→` | Mover pieza |
| `↑` | Rotar pieza |
| `↓` | Caída rápida (soft drop) |
| `Enter` / `Espacio` | Iniciar partida / reiniciar tras game over |

## Estructura del proyecto

```
Tetris_clon/
├── main.py                # Punto de entrada, loop principal (async)
├── game/
│   ├── board.py            # Lógica del tablero: colisiones, líneas, merge
│   ├── config.py           # Constantes: tamaño de grilla, resolución, rutas
│   ├── game.py              # Estado del juego y loop de eventos/render
│   ├── piece.py             # Definición y rotación de las piezas
│   └── scoring.py           # Cálculo de puntuación
├── render/
│   └── renderer.py          # Dibujo de pantallas, tablero, piezas y HUD
├── audio/
│   └── music.py              # Carga y control de la música
├── assets/                  # Imágenes, fuente y audio (.ogg, .png)
├── record                   # Archivo de texto con el récord guardado
└── netlify.toml              # Configuración de build para despliegue web
```

## Cómo correrlo en local

### Requisitos
- Python 3.10 o superior
- pip

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Teakosprey/Tetris_clon.git
   cd Tetris_clon
   ```

2. Instala las dependencias:
   ```bash
   pip3 install pygame
   ```

3. Corre el juego:
   ```bash
   python3 main.py
   ```

Se abrirá una ventana nativa con el juego corriendo directamente sobre tu sistema operativo.

## Cómo funciona la demo web

Pygame no corre de forma nativa en un navegador, así que la demo web no es el mismo `main.py` sirviéndose "tal cual": el proyecto se compila a `WebAssembly` usando `pygbag`, que empaqueta Python + Pygame + los assets en un bundle que el navegador puede ejecutar directamente, sin backend ni servidor Python corriendo detrás.

Para que esto funcione, el loop principal del juego (`main.py` y `game/game.py`) está escrito de forma **asíncrona** (`async def` + `await asyncio.sleep(0)` en cada frame), cediendo control al navegador en cada vuelta para que la pestaña no se congele.

Para probar el build web en tu propia máquina antes de desplegar:

```bash
pip3 install pygbag
python3 -m pygbag .
```

Esto levanta un servidor local (por defecto en `http://localhost:8000`) donde puedes jugar la versión compilada para navegador tal como la verían los visitantes.

## Despliegue en producción

El proyecto se despliega automáticamente en **Netlify**, conectado directamente a este repositorio: cada push a la rama `main` dispara un nuevo build y actualiza el sitio en vivo.

La configuración vive en [`netlify.toml`](./netlify.toml):

```toml
[build]
  command = "pip3 install pygbag && python3 -m pygbag --build ."
  publish = "build/web"
```

- **Build command**: instala `pygbag` y compila el proyecto a WebAssembly
- **Publish directory**: `build/web`, la carpeta que genera pygbag con el `index.html` y los assets empaquetados listos para servir de forma estática

Si quieres desplegar tu propia copia:

1. Haz fork de este repositorio
2. Crea una cuenta en [Netlify](https://netlify.com) y conecta tu fork como nuevo sitio
3. Netlify detectará el `netlify.toml` automáticamente y usará esa configuración de build

## Tecnologías

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/) — motor del juego
- [pygbag](https://github.com/pygame-web/pygbag) — compilación a WebAssembly
- [Netlify](https://www.netlify.com/) — hosting y despliegue continuo
