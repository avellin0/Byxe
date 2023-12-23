# JWT

# Como usar as funções do JWT

*JWT >>> Sign & Verify;*

O JSON Web Token (JWT) é uma ferramenta para codificar informações em um formato seguro e compacto, que pode ser transmitido entre sistemas de forma confiável. Ele é frequentemente usado para autenticação e autorização em aplicativos e sistemas.

*A estrutura de um JWT consiste em três partes: o `cabeçalho (Header), o payload e a assinatura (Signature)`.*

### Header: O cabeçalho do JWT contém informações sobre o tipo de token e o algoritmo de assinatura usado. É um objeto JSON que descreve as características do token, como o tipo ("JWT") e o algoritmo de assinatura.

### Payload: O payload contém os dados do token. Você pode incluir qualquer tipo de informação no payload, como informações de autenticação, autorização ou outros dados relevantes. O payload é o que você deseja transmitir de forma segura entre sistemas. É representado como um objeto JSON.

### Signature: A assinatura é gerada usando a chave secreta (ou uma chave pública, em caso de uso de criptografia assimétrica) e é usada para verificar a autenticidade do token. A assinatura é gerada com base no cabeçalho e no payload, juntamente com a chave secreta. Ela serve para garantir que o token não foi adulterado durante a transmissão.

A função sign é usada para criar um JWT, combinando o cabeçalho, o payload e a assinatura. O token resultante é uma string que pode ser transmitida.

A função verify é usada para verificar a autenticidade do JWT. Ela verifica a assinatura do token, garantindo que ele não tenha sido adulterado e que a chave secreta usada na verificação seja a mesma que foi usada para assinar o token. Se a verificação for bem-sucedida, o resultado será o payload do token decodificado, não um valor booleano.

Portanto, verify não retorna um valor booleano, mas sim o payload do token, desde que a verificação seja bem-sucedida. Se a verificação falhar, ela pode lançar um erro ou retornar null, dependendo da implementação.

Aqui está um exemplo de Verify: `const verificando = verify(token,MY_SECRET_KEY)`

*Lembre-se de usar o DOTENV para pegar o MY_SECRET_KEY da variavel de ambiente*;

## Como funciona o Header.authorization (*auth.ts*)

O código está relacionado à autenticação de solicitações HTTP em uma API usando um token de autenticação no formato "Bearer".

Aqui está o que cada parte do código faz:

1. `const authHeader = req.headers.authorization`: Esta linha obtém o cabeçalho de autorização (authorization) da solicitação HTTP recebida. O cabeçalho de autorização é frequentemente usado para enviar tokens de autenticação.
2. `if (!authHeader || !authHeader.startsWith("Bearer "))`: Esta instrução verifica se o cabeçalho de autorização existe (não é nulo) e se começa com a string "Bearer ". A convenção "Bearer " é comumente usada ao enviar tokens de autenticação no cabeçalho de autorização. Se o cabeçalho de autorização não atender a esses critérios, a API retorna uma resposta com um código de status 401 (Unauthorized) e uma mensagem de erro informando que o token não foi informado.
3. `const token = authHeader.substring(7)`: Se o cabeçalho de autorização atender aos critérios, esta linha extrai o token de autenticação do cabeçalho, removendo os primeiros sete caracteres (a string "Bearer "). O token é então armazenado na variável `token` para uso posterior na autenticação do usuário.

No geral, esse código é usado para garantir que as solicitações à sua API incluam um token de autenticação no cabeçalho de autorização, seguindo a convenção "Bearer". Se o token não estiver presente ou estiver formatado incorretamente, a API responderá com um status 401 e uma mensagem de erro, indicando que a autenticação não foi bem-sucedida. Se o token for válido, ele pode ser usado para autenticar o usuário e autorizar o acesso a recursos protegidos.

# Interface DecodedToken

A declaração interface DecodedToken { UserId: string } define a estrutura esperada do payload do token JWT. Neste caso, você está dizendo ao TypeScript que espera que o payload do token JWT contenha um campo chamado "UserId" que é uma string.

Ao usar as DecodedToken na linha `const decodedToken = verify(token, MY_SECRET_KEY) as DecodedToken`, você está informando explicitamente ao TypeScript que o resultado da função verify deve ser tratado como se tivesse a `estrutura definida na interface DecodedToken`. Isso ajuda o TypeScript a fornecer verificação de tipo e garantir que o decodedToken tenha o formato esperado.

Essa é uma prática comum em TypeScript quando você trabalha com estruturas de dados complexas ou objetos com formatos específicos. Ajuda a tornar o código mais seguro em termos de tipos, evitando erros em tempo de execução relacionados à estrutura dos objetos. Se o resultado da função verify não coincidir com a estrutura definida na interface, o TypeScript gerará um erro de tipo, o que pode ser uma maneira eficaz de pegar erros em tempo de compilação em vez de em tempo de execução.