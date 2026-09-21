help:
	@echo "Comandos disponibles:"
	@echo "  make install   Instala las dependencias del proyecto"
	@echo "  make run       Ejecuta el script principal (p1fia)"
	@echo "  make test      Ejecuta las pruebas"
	@echo "  make lint      Revisa el código con ruff"
	@echo "  make clean     Limpia los archivos temporales"

TARGET = p1fia

# Instalar dependencias
install:
	uv sync

# Ejecutar el script del proyecto
run:
	@uv run $(TARGET)

# Ejecutar pruebas (ejemplo)
test:
	uv run pytest

# Linter (ejemplo con ruff)
lint:
	uv run ruff check .

# Limpieza
clean:
	rm -rf .venv __pycache__ .pytest_cache .ruff_cache

.PHONY: help install run test lint clean
