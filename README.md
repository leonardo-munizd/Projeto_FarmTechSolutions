# 🌱 FarmTech Solutions

Projeto acadêmico desenvolvido para simular uma solução de **Agricultura Digital** utilizando **Python e R**.  
O objetivo é apoiar produtores rurais com cálculos de áreas de plantio, manejo de insumos e integração com dados climáticos em tempo real.

---

## 🚀 Funcionalidades

### 🔹 Aplicação em Python
- Cadastro de **talhões**:
  - **Soja** (área retangular);
  - **Café** (área circular).
- Cálculo automático da área de plantio.
- Cadastro de **manejo de insumos**:
  - Por área (L/ha);
  - Por linha (mL/m).
- Organização dos dados em **vetores**.
- Menu interativo no terminal:
  - Cadastrar / Listar / Atualizar / Deletar dados;
  - Exportar informações para **CSV**.
  
### 🔹 Aplicação em R
- Leitura dos dados exportados do Python (`dados_fazenda.csv`);
- Cálculo de estatísticas básicas:
  - Média;
  - Desvio padrão.
- Conexão com API pública de clima (**OpenWeatherMap**):
  - Consulta em tempo real da **temperatura, umidade e condições do céu**;
  - Exibição simples no terminal.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3**
  - Bibliotecas: `math`, `csv`
- **R**
  - Pacotes: `httr`, `jsonlite`
- **GitHub** para versionamento colaborativo

---


---

## ⚙️ Como Executar

### 🔹 Python
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/farmtech.git
   cd farmtech

#Execute o aplicativo:
python app.py

#Abra o RStudio e rode:
source("analise.R")


