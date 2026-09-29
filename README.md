# AI DevOps Sandbox

Repositorio para el **Proyecto Integrador** del programa AI-Driven DevOps Accelerator.

## Cómo empezar

1. Haz clic en **"Use this template"** (arriba a la derecha del repo en GitHub) para crear tu propia copia. No hagas fork — un template te da un repo limpio, sin historial compartido.
2. En tu copia, abre el repo en **GitHub Codespaces** (botón verde "Code" → "Codespaces" → "Create codespace"). Esto levanta un entorno con Python, Docker y las herramientas necesarias ya instaladas — no importa qué sistema operativo uses en tu laptop.
   - Si prefieres trabajar local, revisa `.devcontainer/devcontainer.json` para ver qué necesitas instalar (Python 3.11+, Docker).
3. Copia `bitacora/template.md` a `bitacora/mi-bitacora.md` y llena el encabezado (Semana 1).
4. Cada semana, entra a la carpeta `labs/semanaN-tema/` correspondiente y lee `scenario.md`. Ahí está el problema de esa semana y qué se espera que documentes.

## Estructura del repo

```
app/                          → la app de ejemplo ("Orders API") que evoluciona semana a semana
bitacora/template.md          → tu bitácora de colaboración con IA (cópiala y llénala)
labs/semana1-setup/           → preparar el entorno (sin problema técnico aún)
labs/semana2-desarrollo-testing/  → bug de lógica + tests fallidos
labs/semana3-cicd/            → pipeline de GitHub Actions roto
labs/semana4-cloud-iac/       → Terraform con configuración riesgosa
labs/semana5-agentes/         → esqueleto de un agente a completar
labs/semana6-observabilidad/  → logs con una anomalía a detectar
labs/semana7-runbooks-chatops/→ escenario de incidente para generar un runbook
labs/semana8-devsecops/       → manifiesto con problemas de seguridad intencionales
```

## Dos rutas posibles

- **Ruta A — Reto guiado (este sandbox):** trabaja los labs de este repo tal cual.
- **Ruta B — Problema propio:** si tienes un caso real de tu trabajo, solo necesitas `bitacora/template.md` — no tienes que usar los labs de `labs/`, pero sí debes producir el mismo tipo de entradas semanales.

## Importante

- No subas credenciales, tokens, ni datos reales de ningún cliente o empresa a este repo, ni siquiera en tu copia privada.
- Los labs de Terraform usan [LocalStack](https://www.localstack.cloud/) para simular AWS localmente — no necesitas una cuenta cloud real.
- Si algo no aplica a tu proyecto en una semana determinada, documéntalo en tu bitácora explicando por qué, en vez de omitirlo.
