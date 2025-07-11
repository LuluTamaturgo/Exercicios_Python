🗂️ Tabela fnde_data_eex
Esta tabela armazena informações de adesão de escolas a um programa ou módulo do FNDE identificado pela sigla “EEX”, bem como o acompanhamento da prestação de contas correspondente.

📑 Estrutura da Tabela

| Campo              | Tipo       | Chave / Restrição   | Descrição                                                                                                                                                                   | Relacionamento Sugerido                |
| ------------------ | ---------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `id`               | `bigint`   | PK, auto\_increment | Identificador técnico exclusivo da linha. Utilizado como chave primária para indexação.                                                                                     | -                                      |
| `adesao_status`    | `longtext` | NOT NULL            | Texto descritivo da situação da adesão da escola ao programa EEX. Pode conter valores como “Solicitada”, “Aprovada”, “Reprovada” ou “Em análise”.                           | -                                      |
| `adesao_data`      | `date`     | NULL                | Data em que a adesão foi efetivada ou registrada. Se não houver adesão ainda, este campo permanece nulo.                                                                    | -                                      |
| `prestacao_contas` | `longtext` | NULL                | Campo livre para observações sobre a prestação de contas. Pode conter texto descritivo, link de documentos ou até JSON estruturado.                                         | -                                      |
| `escola_id`        | `bigint`   | UNIQUE, NOT NULL    | Referência única para a escola que aderiu ao programa. Cada escola pode ter **apenas um** registro ativo de adesão. Provável **chave estrangeira para `fnde_data_escola`**. | 🔗 `fnde_data_escola.id` (FK sugerida) |

🔗 Relacionamentos

| Campo       | Tabela Relacionada | Tipo de Relacionamento    | Observação                                                                |
| ----------- | ------------------ | ------------------------- | ------------------------------------------------------------------------- |
| `escola_id` | `fnde_data_escola` | 🔑 Chave estrangeira (FK) | Cada escola pode ter **uma única adesão ativa** no programa EEX (UNIQUE). |


### Índices
- Index em (`id`,`adesao_status`, `adesao_data`, `prestacao_contas`, `escola_id`) conforme definido em `Meta.indexes`.