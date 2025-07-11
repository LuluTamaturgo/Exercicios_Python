🗂️ Tabela fnde_data_convenio
Esta tabela consolida dados de convênios e repasses celebrados entre o FNDE e as entidades executoras (prefeituras, secretarias ou escolas). Ela é útil para acompanhar a situação, a fase do processo, valores já pagos, vigência do convênio e outras informações‑chave que aparecem nos portais SIGECON/Contas Online.

📑 Estrutura da Tabela

| Campo                    | Tipo         | Chave         | Descrição                                                                                               | Possível Relacionamento                       |
| ------------------------ | ------------ | ------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `id`                     | bigint       | PK, auto\_inc | Identificador técnico único da linha.                                                                   | -                                             |
| `liberadaContasOnline`   | varchar(1)   | NOT NULL      | Indica se a conta do convênio está liberada para movimentação/prestação no sistema Contas Online (S/N). | -                                             |
| `faseId`                 | varchar(10)  | NOT NULL      | Código da fase processual do convênio. Exemplo: “08” = Em execução.                                     | 🔗 `faseNome` (espelho)                       |
| `entidadeId`             | varchar(20)  | NOT NULL      | Código da entidade executora no FNDE.                                                                   | Pode se relacionar com cadastro institucional |
| `situacaoId`             | varchar(10)  | NOT NULL      | Código da situação do convênio.                                                                         | 🔗 `situacaoNome` (espelho)                   |
| `entidadeCnpj`           | varchar(20)  | NULL          | CNPJ da entidade executora.                                                                             | 🔗 `fnde_data_cnpjmunicipio.cnpj`             |
| `tipoConcessaoId`        | varchar(10)  | NOT NULL      | Código do tipo de concessão (repasse, termo de compromisso, etc.).                                      | 🔗 `tipoConcessaoNome`                        |
| `codIbge`                | varchar(10)  | NOT NULL      | Código IBGE do município. Permite cruzamento geográfico.                                                | 🔗 `fnde_data_municipiofnde.municipio_codigo` |
| `fimVigenciaConvenio`    | varchar(20)  | NOT NULL      | Data final da vigência do convênio (texto).                                                             | -                                             |
| `pcId`                   | varchar(20)  | NOT NULL      | Código da prestação de contas vinculada.                                                                | 🔗 Tabela de prestações de contas             |
| `tipoConcessaoNome`      | varchar(100) | NOT NULL      | Nome do tipo de concessão (ex.: “Convênio”, “Repasse direto”).                                          | Espelho de `tipoConcessaoId`                  |
| `tipoConcessaoConvenio`  | tinyint(1)   | NOT NULL      | 1 = é convênio; 0 = outro tipo (ex.: termo).                                                            | -                                             |
| `colId`                  | varchar(10)  | NOT NULL      | Código da Conta Online do convênio.                                                                     | 🔗 Sistema Contas Online                      |
| `fimVigenciaConvenioAno` | varchar(10)  | NOT NULL      | Ano da vigência final (redundante, usado em filtros).                                                   | -                                             |
| `situacaoPCId`           | varchar(10)  | NOT NULL      | Código da situação da prestação de contas.                                                              | 🔗 `situacaoPCNome`                           |
| `faseNome`               | varchar(100) | NOT NULL      | Nome da fase processual (espelha `faseId`).                                                             | -                                             |
| `ufNome`                 | varchar(10)  | NOT NULL      | Unidade federativa (UF) da entidade executora.                                                          | -                                             |
| `pcIncluida`             | varchar(10)  | NOT NULL      | Indica se a prestação de contas foi incluída (S/Não).                                                   | -                                             |
| `tipoConcessaoRepasse`   | tinyint(1)   | NOT NULL      | Flag: 1 = repasse direto; 0 = não repasse.                                                              | -                                             |
| `programaId`             | varchar(10)  | NOT NULL      | Código do programa financiador (ex.: 2082 = PDDE).                                                      | 🔗 `programaNome`                             |
| `anoConcessao`           | varchar(10)  | NOT NULL      | Ano de concessão do recurso.                                                                            | -                                             |
| `situacaoNome`           | varchar(100) | NOT NULL      | Nome descritivo da situação do convênio. Espelha `situacaoId`.                                          | -                                             |
| `entidadeNome`           | varchar(255) | NOT NULL      | Nome oficial da entidade executora.                                                                     | 🔗 `entidadeId`                               |
| `dataAssinaturaConvenio` | varchar(20)  | NOT NULL      | Data de assinatura do convênio ou termo (texto).                                                        | -                                             |
| `municipioId`            | varchar(10)  | NOT NULL      | Código interno do município do convênio.                                                                | 🔗 `fnde_data_municipiofnde.municipio_codigo` |
| `valorTotalPago`         | varchar(20)  | NOT NULL      | Valor total já repassado.                                                                               | Pode precisar conversão para tipo numérico    |
| `totalRegistros`         | varchar(20)  | NOT NULL      | Número total de repasses vinculados.                                                                    | -                                             |
| `demandaMonitorada`      | tinyint(1)   | NOT NULL      | Indica se o convênio está sob monitoramento especial.                                                   | -                                             |
| `tipoBotao`              | int          | NOT NULL      | Código para exibição de botões em interface (ex.: exibir detalhes, prestação etc.).                     | Usado em portais                              |
| `permiteAcessoSigecon`   | varchar(10)  | NOT NULL      | Indicador (S/N) de acesso liberado ao SIGECON.                                                          | -                                             |
| `programaNome`           | varchar(100) | NOT NULL      | Nome do programa financiador. Espelha `programaId`.                                                     | -                                             |
| `municipioNome`          | varchar(100) | NOT NULL      | Nome do município. Uso para exibição em relatórios.                                                     | Espelho de `municipioId`                      |
| `situacaoPCNome`         | varchar(100) | NOT NULL      | Nome da situação da prestação de contas. Espelha `situacaoPCId`.                                        | -                                             |
| `efeitoSuspensivo`       | varchar(255) | NULL          | Motivo do bloqueio/suspensão do convênio, se houver.                                                    | -                                             |
| `medidaExcecao`          | varchar(255) | NULL          | Medidas excepcionais adotadas (reprogramações, prorrogações etc).                                       | -                                             |

🔗 Relacionamentos Relevantes

| Campo          | Tabela Relacionada                         | Tipo de Relacionamento |
| -------------- | ------------------------------------------ | ---------------------- |
| `entidadeCnpj` | `fnde_data_cnpjmunicipio.cnpj`             | FK lógica              |
| `municipioId`  | `fnde_data_municipiofnde.municipio_codigo` | FK lógica              |
| `codIbge`      | `fnde_data_municipiofnde.municipio_codigo` | FK lógica              |
| `programaId`   | Tabela de programas do FNDE                | Chave de negócio       |
| `pcId`         | Tabela de prestações de contas             | Chave de negócio       |


### Índices
- Index em (`id`, `liberadaContasOnline`, `faseId`, `entidadeId`,`situacaoId`,`entidadeCnpj`,`tipoConcessaoId`,`codIbge`,`fimVigenciaConvenio`,`pcId`,`tipoConcessaoNome`,`tipoConcessaoConvenio`,`colId`,`fimVigenciaConvenioAno`,`situacaoPCId`,`faseNome`,`ufNome`,`pcIncluida`,`tipoConcessaoRepasse`,`programaId`,`anoConcessao`,`situacaoNome`,`entidadeNome`,`dataAssinaturaConvenio`,`municipioId`,`valorTotalPago`,`totalRegistros`,`demandaMonitorada`,`tipoBotao`,`permiteAcessoSigecon`,`programaNome`,`municipioNome`,`situacaoPCNome`,`efeitoSuspensivo`,`medidaExcecao`) conforme definido em `Meta.indexes`.