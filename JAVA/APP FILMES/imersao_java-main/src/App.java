import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.List;
import java.util.Map;

public class App {
    /**
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
     
        // Abrir conexão HTTP e buscar os Top 250 filmes do IMDB-API
        String url = "https://mocki.io/v1/9a7c1ca9-29b4-4eb3-8306-1adb9d159060";
        URI endereco = URI.create(url);
        var client = HttpClient.newHttpClient();
        var request = HttpRequest.newBuilder(endereco).GET().build();
        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        String body = response.body();
        System.out.println(body);
        
        //extrair os dados que interessam da API (titulo, poster, classificação)
        var parser = new JsonParser();
        List<Map<String, String>> listaDeFilmes = parser.parse(body);

        //exibir e manipuldar os dados
        for (Map<String,String> filme : listaDeFilmes) {
            System.out.println("\u001b[37m\u001b[42mNome do Filme:\u001b[m" + filme.get("title"));
            System.out.println("Imagem do Filme: " + filme.get("image"));
            System.out.println("Nota do Filme: " + "\u001b[46m"+filme.get("imDbRating")+"\u001b[m");
            System.out.println("Avaliação: "+"\u2B50".repeat(5));
            System.out.println();
        }
    }
}
