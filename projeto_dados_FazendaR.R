# Ler CSV
dados <- read.csv("dados_fazenda.csv", sep = ",", dec = ".", stringsAsFactors = FALSE)

# Conferir
print(dados)


# Talhões (apenas linhas onde Tipo == "Talhao")
talhoes <- subset(dados, Tipo == "Talhao")

# Converter área para numérica
talhoes$Area_m2 <- as.numeric(talhoes$Area_m2)
talhoes$Area_ha <- talhoes$Area_m2 / 10000

media_area <- mean(talhoes$Area_ha, na.rm = TRUE)
desvio_area <- sd(talhoes$Area_ha, na.rm = TRUE)

cat("📊 Média da área (ha):", media_area, "\n")
cat("📊 Desvio padrão da área (ha):", desvio_area, "\n")
