import 'package:flutter/material.dart';

void main() => runApp(Emotion2CodeApp());

class Emotion2CodeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Emotion2Code',
      home: Scaffold(
        appBar: AppBar(title: Text('Emotion2Code')),
        body: Center(child: Text('💡 Mobile version coming soon!')),
      ),
    );
  }
}
