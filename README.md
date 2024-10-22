Este código é um sistema simples de venda de passagens aéreas, permitindo a reserva de assentos e o cálculo do faturamento do voo. Ele realiza as seguintes funções:

### Resumo de Funcionamento:

1. **Reservar Passagens:**
   - O código permite ao usuário selecionar quantas passagens deseja comprar.
   - O usuário escolhe a fileira (A, B, C, D) e o número do assento (1 a 20).
   - Se o assento estiver disponível, ele é reservado. Caso contrário, o usuário deve selecionar outro.

2. **Desconto por Idade:**
   - Se o passageiro tiver menos de 5 anos ou mais de 65, ele recebe um desconto de 50% no valor da passagem.
   - O valor padrão da passagem é R$ 1500.

3. **Controle de Faturamento e Ocupação:**
   - A cada compra, o valor da passagem (com ou sem desconto) é adicionado ao faturamento total.
   - O sistema calcula a taxa de ocupação com base no número de assentos vendidos e verifica se o voo pode ser realizado.

4. **Verificação do Voo:**
   - Se menos de 35 passagens forem vendidas, o voo é cancelado, e o valor faturado é devolvido.
   - Caso a ocupação seja suficiente, o voo é autorizado e o faturamento total é exibido.

### Objetivo:
Este sistema simula o processo de reserva de passagens, gerenciamento de ocupação de assentos e cálculo de faturamento de um voo, proporcionando ao usuário a experiência de compra de passagens, além de lidar com possíveis descontos e a verificação de viabilidade do voo.

Este código poderia ser usado em um contexto educacional ou para pequenas simulações de vendas e reservas de assentos.
