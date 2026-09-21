help:
	@echo "Comandos disponibles:"
	@echo "  make install   Instala las dependencias del proyecto"
	@echo "  make run       Ejecuta el script principal"
	@echo "  make clean     Limpia los archivos temporales"

TARGET = practica01

# Instalar dependencias
install:
	uv sync

# Ejecutar el script del proyecto
run:
	@uv run $(TARGET)

clean:
	rm -rf .venv __pycache__ .pytest_cache .ruff_cache

.PHONY: help install run clean
