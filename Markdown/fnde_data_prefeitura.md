Tabela: fnde_data_prefeitura
A tabela fnde_data_prefeitura armazena informações institucionais e de contato de prefeituras municipais, incluindo dados administrativos, dados do prefeito (representante legal do município), e dados de atualização. Essa estrutura permite acompanhar e validar os dados de governança local em sistemas de repasse, fiscalização e acompanhamento de programas do FNDE e demais órgãos federais.

| Campo                  | Tipo           | Obrigatório | Observações                                                                                          |
| ---------------------- | -------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| **id**                 | `bigint`       | Sim (PK)    | Identificador único da prefeitura no sistema. Gerado automaticamente (`auto_increment`).             |
| **nome**               | `varchar(255)` | Sim         | Nome fantasia da prefeitura ou nome usado em sistemas do FNDE (ex: “Prefeitura Municipal de X”).     |
| **cnpj**               | `varchar(25)`  | Sim         | Número do CNPJ da prefeitura. Responsável jurídico pelo município.                                   |
| **telefone**           | `varchar(40)`  | Sim         | Telefone geral de contato da prefeitura.                                                             |
| **email**              | `varchar(120)` | Sim         | E-mail institucional de contato da prefeitura.                                                       |
| **atualizado\_em**     | `datetime(6)`  | Sim         | Data e hora da última atualização dos dados do registro. Permite controle de versão e sincronização. |
| **razao\_social**      | `varchar(255)` | Sim         | Razão social oficial da prefeitura conforme consta no CNPJ.                                          |
| **prefeito\_cpf**      | `varchar(20)`  | Sim         | CPF do(a) prefeito(a) atual. Usado para validações legais e cruzamento com outros sistemas.          |
| **prefeito\_email**    | `varchar(120)` | Sim         | E-mail pessoal ou funcional do(a) prefeito(a).                                                       |
| **prefeito\_nome**     | `varchar(120)` | Sim         | Nome completo do(a) prefeito(a).                                                                     |
| **estado**             | `varchar(30)`  | Sim         | Nome do estado (ex: “Bahia”, “Paraná”).                                                              |
| **municipio**          | `varchar(80)`  | Sim         | Nome do município correspondente.                                                                    |
| **prefeito\_rg**       | `varchar(30)`  | Sim         | Número do RG do(a) prefeito(a). Pode ser usado em validações de identidade.                          |
| **prefeito\_telefone** | `varchar(40)`  | Sim         | Telefone de contato direto do(a) prefeito(a).                                                        |

🔗 Possíveis Relacionamentos

Município:

O campo municipio (nome do município) pode ser relacionado a uma tabela padrão de municípios, como fnde_data_municipiofnde ou fnde_data_municipiosiscacs para padronização e integridade referencial, idealmente via chave estrangeira (não presente explicitamente aqui, mas recomendado para modelo relacional).

Prefeito:

Os dados do prefeito (CPF, RG, nome, telefone, e-mail) podem ser cruzados com outras tabelas ou sistemas que contenham informações de gestores públicos (ex.: fnde_data_prefeitodirigente).

### Índices
- Index em (`id`,`nome`,`cnpj`,`telefone`,`email`,`atualizado_em`,`razao_social`,`prefeito_cpf`,`prefeito_email`,`prefeito_nome`,`estado`,`municipio`,`prefeito_rg`,`prefeito_telefone`) conforme definido em `Meta.indexes`.