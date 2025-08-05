import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const MLModelApp());
}

class MLModelApp extends StatelessWidget {
  const MLModelApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ML Model Showcase',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        scaffoldBackgroundColor: const Color(0xFFF6F8FE),
      ),
      home: const HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
