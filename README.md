# ept
Algoritmo e Python para Cálculo de Estado Plano de Tensões e Deformações

# Estado Plano de Tensões e Círculo de Mohr

O **estado plano de tensões** é um conceito de reistência dos materiais. Ele descreve a condição na qual um objeto ou material está sujeito a tensões em apenas dois planos perpendiculares. Geralmente, isso ocorre em estruturas ou componentes que têm uma dimensão muito maior em uma direção do que em outras.

## Círculo de Mohr

O **círculo de Mohr** é uma ferramenta gráfica poderosa usada para representar e analisar o estado de tensões em um material. Desenvolvido pelo engenheiro civil alemão Christian Otto Mohr no final do século XIX, o círculo de Mohr oferece uma maneira intuitiva de visualizar as tensões principais e as direções principais em um material submetido a um estado plano de tensões.

### Como funciona o círculo de Mohr:

1. **Identificação das tensões principais**: As tensões normais e de cisalhamento nos planos originais são representadas em um gráfico de eixos cartesianos, onde os eixos são as tensões normais (vertical) e as tensões de cisalhamento (horizontal).

2. **Construção do círculo**: Com base nessas tensões, o círculo de Mohr é desenhado, com o centro localizado no ponto médio do segmento de linha que conecta as tensões normais e uma linha de diâmetro perpendicular a esse segmento.

3. **Localização das tensões principais**: Os diâmetros do círculo representam as tensões principais. Os pontos onde esses diâmetros interceptam o círculo indicam as magnitudes e as direções das tensões principais.

4. **Determinação das direções principais**: As direções principais são perpendiculares aos diâmetros do círculo, passando pelos pontos correspondentes às tensões principais.

### Aplicações do círculo de Mohr:

- **Projeto de estruturas**: Permite aos engenheiros entender como as tensões estão distribuídas em diferentes partes de uma estrutura e projetar materiais que resistam a essas tensões de maneira eficaz.

- **Análise de falhas**: Ajuda a identificar os locais onde as tensões são mais críticas, auxiliando na prevenção de falhas em materiais e componentes.

- **Otimização de materiais**: Permite ajustar geometrias e materiais para minimizar as tensões máximas e, assim, melhorar o desempenho e a durabilidade das estruturas.


Essa aplicação escrita em Python para a disciplina de Mecânica dos Sólidos, resolve alguns problemas referentes a resistência dos materiais. 
