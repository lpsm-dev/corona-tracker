# REST APIs with Flask-RestPlus

Ao contrário do Django, o Flask não vem como um padrão a ser seguido, mas a um ecossistema inteiro de bibliotecas de código aberto disponibilizados pela comunidade. Uma dessas bibliotecas é o Flask-RestPlus.

O Flask-RestPlus é uma biblioteca de extensão do Flask e, como o nome sugere, ajuda a facilitar a criação de APIS Restful estruturadas com configuração mínima e incentivo as melhores práticas. 

Se você está familiarizado com o Flask, o Flask-RestPlus deve ser fácil de pegar. Ele fornece uma coleção coerente de decoradores e ferramentas para desenvolver sua API e expor sua documentação adequadamente (utilizando o Swagger).

Apesar de seguir certas converções, o Flask-RestPlus não insiste nelas, com o Django. De certa forma, o Flask-RestPlus tenta ajudar a organizar um projeto crescente do Flask, mas sem perder sua sobrecarga mínima, que é o maior charme do Flask.

## Namespaces

Os namespaces são opcionais e adicionam um pouco de toque organizacional à API que você está construindo, principalmente do ponto de vista da documentação. Um namespace permite agrupar resources relacionados em uma raiz comum.

```python
namespace_conferences = api.namespace("conferences", description="Conference operations")
```

Para trazer um recurso para um namespace, tudo que você precisa fazer é substituir o Decorator da sua rota mapeada na classe, para o namespace criado.

## Blueprints

O Flask utiliza um conceito de Blueprints para criar componentes de aplicativos e suportar padrões comuns dentro de um aplicativo ou entre aplicativos. 

Um objeto Blueprint funciona de maneira semelhante a um objeto Flask de aplicativo, mas na verdade não é um aplicativo. Pelo contrário, é um plano de como construir ou estender um aplicativo.

Portanto, as Blueprints se tornaram uma maneira popular de projetar aplicativos modulares. O mesmo se aplica ao Flask-RestPlus.
