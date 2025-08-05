import 'package:flutter/material.dart';
import '../services/api_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController _inputController = TextEditingController();
  String? predictionResult;
  bool loading = false;

  void handlePredict() async {
    setState(() => loading = true);
    final response = await ApiService.predict(
      modelName: "text-sentiment-model",
      inputText: _inputController.text.trim(),
    );
    setState(() {
      predictionResult = response;
      loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('ML Model Deployment Showcase'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _inputController,
              maxLines: 5,
              decoration: InputDecoration(
                hintText: 'Enter input text...',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: loading ? null : handlePredict,
              child: loading
                  ? const CircularProgressIndicator()
                  : const Text('Send to Model'),
            ),
            const SizedBox(height: 24),
            if (predictionResult != null)
              Text(
                'Prediction: $predictionResult',
                style: const TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.w600,
                ),
              ),
          ],
        ),
      ),
    );
  }
}
