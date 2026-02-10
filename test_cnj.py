import requests
import json
import re

# 1. Configurações Globais da API Pública
API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
HEADERS = {
    "Authorization": f"APIKey {API_KEY}",
    "Content-Type": "application/json"
}

# 2. Mapa simplificado de Tribunais (Endpoints)
# O número CNJ tem o formato: NNNNNNN-DD.AAAA.J.TR.OOOO
# J = Justiça (8 = Estadual, 5 = Federal, etc)
# TR = Tribunal (26 = SP, 19 = RJ, etc)
def obter_endpoint(j, tr):
    if j == '8': # Justiça Estadual
        if tr == '26': return "api_publica_tjsp"
        if tr == '19': return "api_publica_tjrj"
        if tr == '13': return "api_publica_tjmg"
        if tr == '21': return "api_publica_tjrs"
    elif j == '5': # Justiça Federal
        return f"api_publica_trf{tr}"
    elif j == '3': # Tribunal Superior (STJ)
        return "api_publica_stj"
    
    # Fallback: Tenta montar o padrão (ex: api_publica_tjam)
    # Mas o ideal é ter um mapa completo num arquivo separado
    return None

def consultar_processo_cnj(numero_processo):
    # Remove pontos e traços
    numero_limpo = re.sub(r'\D', '', numero_processo)
    
    # Extrai J e TR (Posições fixas no CNJ de 20 dígitos)
    # NNNNNNN-DD.AAAA.J.TR.OOOO -> O J é o 14º dígito, TR são 15º e 16º
    # Ex: 0000000002023 8 26 0000
    if len(numero_limpo) < 20:
        print("Erro: Número de processo inválido (menos de 20 dígitos).")
        return

    j = numero_limpo[13:14]
    tr = numero_limpo[14:16]
    
    endpoint_suffix = obter_endpoint(j, tr)
    
    if not endpoint_suffix:
        print(f"Tribunal (J={j}, TR={tr}) não mapeado neste script de teste.")
        return

    url = f"https://api-publica.datajud.cnj.jus.br/{endpoint_suffix}/processo/pesquisa"
    
    payload = {
        "query": {
            "match": {
                "numeroProcesso": numero_limpo
            }
        }
    }

    print(f"📡 Consultando API: {url}")
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            dados = response.json()
            hits = dados.get('hits', {}).get('hits', [])
            
            if hits:
                processo = hits[0]['_source']
                print("\n✅ PROCESSO ENCONTRADO!")
                print(f"Tribunal: {processo.get('tribunal')}")
                print(f"Classe: {processo.get('classe', {}).get('nome')}")
                print(f"Última atualização: {processo.get('dataHoraUltimaAtualizacao')}")
                
                # Listar últimos 3 movimentos
                movimentos = processo.get('movimentos', [])
                print("\n--- Últimos Movimentos ---")
                for mov in sorted(movimentos, key=lambda x: x.get('dataHora'), reverse=True)[:3]:
                    print(f"[{mov.get('dataHora')}] {mov.get('nome')}")
            else:
                print("❌ Processo não encontrado na base do DataJud.")
        else:
            print(f"Erro na requisição: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Erro de conexão: {e}")

# Teste com um processo público real (Exemplo do TJSP)
# Se não funcionar, troque por um número de processo que você conhece
if __name__ == "__main__":
    numero = input("Digite o número do processo (formato CNJ): ")