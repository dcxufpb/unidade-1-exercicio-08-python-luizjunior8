# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual


def dados_loja_objeto(loja):
    if not loja.nome_loja:
        raise Exception("O campo nome da loja é obrigatório")

    if not loja.logradouro:
        raise Exception("O campo logradouro do endereço é obrigatório") 

    _numero = "s/n" if not loja.numero else str(loja.numero)

    if not loja.municipio:
        raise Exception("O campo município do endereço é obrigatório")  

    if not loja.estado:
        raise Exception("O campo estado do endereço é obrigatório") 

    if not loja.cnpj:
        raise Exception("O campo CNPJ da loja é obrigatório") 

    if not loja.inscricao_estadual:
        raise Exception("O campo inscrição estadual da loja é obrigatório")  


    _complemento = ""

    if loja.complemento:
       _complemento = " " + loja.complemento


    _bairro = ""

    if loja.bairro:
        _bairro = loja.bairro + " - "

    _cep = ""
    _telefone = ""

    if loja.cep:
        _cep = "CEP:" + loja.cep

        if loja.telefone:
            _telefone = " Tel " + loja.telefone

    else:
        _telefone = "Tel " + loja.telefone


    _observacao = ""

    if loja.observacao:
        _observacao = loja.observacao

    typewriter = loja.nome_loja + "\n"
    typewriter += loja.logradouro + ", " + _numero + _complemento + "\n"
    typewriter += _bairro + loja.municipio + " - " + loja.estado + "\n"
    typewriter += _cep + _telefone + "\n"
    typewriter += _observacao + "\n"
    typewriter += "CNPJ: " + loja.cnpj + "\n"
    typewriter += "IE: " + loja.inscricao_estadual

    return typewriter
