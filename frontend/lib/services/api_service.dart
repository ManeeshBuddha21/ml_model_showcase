import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:8000/api'; // Update if backend runs elsewhere

  static Future<String> predict({
    required String modelName,
    required String inputText,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/predict'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'model_name': modelName,
          'input_text': inputText,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return '${data["prediction"]} (${(data["confidence"] * 100).toStringAsFixed(1)}%)';
      } else {
        return 'Error: ${response.statusCode}';
      }
    } catch (e) {
      return 'Request failed: $e';
    }
  }
}
