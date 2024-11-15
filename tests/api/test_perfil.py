import pytest
import httpx
from unittest.mock import patch

@pytest.mark.asyncio
@pytest.mark.skip(reason="ver tiempo de ejecución usando mock") 
async def test_perfil_endpoint():
    url = "https://jimcostdev.koyeb.app/perfil/jimcostdev"
    
    # Realizar la solicitud HTTP
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    # Verificar que la respuesta tenga un código de estado 200
    assert response.status_code == 200

    # Verificar que la respuesta tenga el contenido esperado
    expected_response = {
        "rol": "Software Engineer",
        "description": "Soy Ingeniero Informático con sólida experiencia en el desarrollo de software y un enfoque especializado en desarrollo web utilizando Python y JavaScript. A lo largo de mi carrera, me he destacado no solo por mis habilidades técnicas, sino también por mi capacidad para enseñar, lo que me ha permitido ejercer como docente y tutor de programación, acompañando a estudiantes en su formación.\n\nAdemás, cuento con certificaciones como: MongoDB Associate Developer, Associate DBA y Microsoft Azure Fundamentals, lo que respalda mis conocimientos en tecnologías de bases de datos y entornos en la nube.",
        "skills": [
            "python",
            "javascript",
            "go",
            "fastapi",
            "django",
            "tailwind",
            "astro",
            "react",
            "mongodb",
            "postgresql",
            "sqlserver",
            "git"
        ],
        "username": "jimcostdev",
        "avatar": "https://avatars.githubusercontent.com/u/53100460?v=4",
        "id": 1
    }
    assert response.json() == expected_response
 
# Usa pytest-mock o el decorador patch de unittest para simular la solicitud
@patch("httpx.Client.get")
def test_perfil_endpoint_mock(mock_get):
    # Configuramos el mock para devolver una respuesta simulada
    mock_response = httpx.Response(
        status_code=200,
        json={
            "rol": "Software Engineer",
            "description": "Soy Ingeniero Informático con sólida experiencia en el desarrollo de software.",
            "skills": ["python", "javascript", "fastapi"],
            "username": "jimcostdev",
            "avatar": "https://avatars.githubusercontent.com/u/53100460?v=4",
            "id": 1
        }
    )
    mock_get.return_value = mock_response

    # Simula el cliente HTTP
    with httpx.Client() as client:
        response = client.get("https://ficticious-url.local/test-endpoint")

    # Comprueba que los datos sean correctos
    assert response.status_code == 200
    assert response.json()["username"] == "jimcostdev"