import asyncio
import httpx
from django.http import HttpResponse

async def contador_async(request):
    output = ""

    # Contador de 1 a 5 com 1 segundo entre cada número
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)  # aparece no terminal
        output += f"{num}\n"

    # Requisição HTTP para um endpoint confiável
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.github.com")
        output += "\n--- Resposta da API ---\n"
        output += r.text

    return HttpResponse(f"<pre>{output}</pre>")