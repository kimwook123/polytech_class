import 'dart:math' as math;
import 'package:flutter/material.dart';

void main() {
  runApp(const CalculatorApp());
}

class CalculatorApp extends StatelessWidget {
  const CalculatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Stack Calculator',
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF0F172A),
      ),
      home: const CalculatorHome(),
    );
  }
}

class CalculatorHome extends StatefulWidget {
  const CalculatorHome({super.key});

  @override
  State<CalculatorHome> createState() => _CalculatorHomeState();
}

class _CalculatorHomeState extends State<CalculatorHome> {
  String _expression = '';
  String _result = '0';

  void _appendToken(String token) {
    setState(() {
      if (_expression.isEmpty && _isOperator(token) && token != '-') {
        return;
      }

      if (_expression == 'Error') {
        _expression = '';
      }

      if (token == '⌫') {
        if (_expression.isNotEmpty) {
          _expression = _expression.substring(0, _expression.length - 1);
        }
        if (_expression.isEmpty) {
          _result = '0';
        }
        return;
      }

      if (token == 'C') {
        _expression = '';
        _result = '0';
        return;
      }

      if (token == '=') {
        try {
          final value = StackCalculator.evaluate(_expression);
          _result = _formatResult(value);
          _expression = _expression;
        } catch (_) {
          _expression = 'Error';
          _result = '0';
        }
        return;
      }

      _expression += token;
    });
  }

  bool _isOperator(String token) {
    return ['+', '−', '×', '÷', '%', '^', '(', ')'].contains(token);
  }

  String _formatResult(double value) {
    if (value == value.toInt()) {
      return value.toInt().toString();
    }
    return value.toString();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Expanded(
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: const Color(0xFF1E293B),
                    borderRadius: BorderRadius.circular(24),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Text(
                        _expression.isEmpty ? '0' : _expression,
                        style: const TextStyle(
                          color: Colors.white70,
                          fontSize: 28,
                        ),
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 12),
                      Text(
                        _result,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 52,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 20),
              _buildKeypad(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildKeypad() {
    final rows = [
      ['C', '⌫', '%', '÷'],
      ['7', '8', '9', '×'],
      ['4', '5', '6', '−'],
      ['1', '2', '3', '+'],
      ['(', '0', ')', '='],
    ];

    return Column(
      children: rows.map((row) {
        return Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: Row(
            children: row.map((label) {
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 6),
                  child: _KeyButton(
                    label: label,
                    onTap: () => _appendToken(label),
                  ),
                ),
              );
            }).toList(),
          ),
        );
      }).toList(),
    );
  }
}

class _KeyButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;

  const _KeyButton({required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final bool isOperator = ['+', '−', '×', '÷', '%', '^', '(', ')', 'C', '⌫'].contains(label);
    final bool isEqual = label == '=';

    Color backgroundColor = isEqual
        ? const Color(0xFF06B6D4)
        : isOperator
            ? const Color(0xFF334155)
            : const Color(0xFF1E293B);

    Color textColor = isEqual ? Colors.black : Colors.white;

    return SizedBox(
      height: 64,
      child: Material(
        color: backgroundColor,
        borderRadius: BorderRadius.circular(16),
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: onTap,
          child: Center(
            child: Text(
              label,
              style: TextStyle(
                color: textColor,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class StackCalculator {
  static const Map<String, int> _precedence = {
    '+': 1,
    '−': 1,
    '×': 2,
    '÷': 2,
    '%': 2,
    '^': 3,
  };

  static double evaluate(String expression) {
    final tokens = _tokenize(expression);
    final postfix = _toPostfix(tokens);
    return _evaluatePostfix(postfix);
  }

  static List<String> _tokenize(String expression) {
    final sanitized = expression
        .replaceAll('×', '*')
        .replaceAll('−', '-')
        .replaceAll('÷', '/')
        .replaceAll(' ', '');

    final tokens = <String>[];
    int index = 0;

    while (index < sanitized.length) {
      final char = sanitized[index];

      if (RegExp(r'[0-9.]').hasMatch(char)) {
        final start = index;
        while (index < sanitized.length && RegExp(r'[0-9.]').hasMatch(sanitized[index])) {
          index++;
        }
        tokens.add(sanitized.substring(start, index));
        continue;
      }

      if (RegExp(r'[+\-*/%^()]').hasMatch(char)) {
        tokens.add(char);
        index++;
        continue;
      }

      throw FormatException('Invalid character: $char');
    }

    return tokens;
  }

  static List<String> _toPostfix(List<String> tokens) {
    final output = <String>[];
    final ops = <String>[];

    for (final token in tokens) {
      if (RegExp(r'^\d+(\.\d+)?$').hasMatch(token)) {
        output.add(token);
      } else if (token == '(') {
        ops.add(token);
      } else if (token == ')') {
        while (ops.isNotEmpty && ops.last != '(') {
          output.add(ops.removeLast());
        }
        if (ops.isEmpty || ops.removeLast() != '(') {
          throw FormatException('Mismatched parentheses');
        }
      } else {
        while (ops.isNotEmpty &&
            _precedence.containsKey(ops.last) &&
            _precedence[ops.last]! >= _precedence[token]!) {
          output.add(ops.removeLast());
        }
        ops.add(token);
      }
    }

    while (ops.isNotEmpty) {
      final op = ops.removeLast();
      if (op == '(' || op == ')') {
        throw FormatException('Mismatched parentheses');
      }
      output.add(op);
    }

    return output;
  }

  static double _evaluatePostfix(List<String> postfix) {
    final stack = <double>[];

    for (final token in postfix) {
      if (RegExp(r'^\d+(\.\d+)?$').hasMatch(token)) {
        stack.add(double.parse(token));
      } else {
        if (stack.length < 2) {
          throw FormatException('Invalid expression');
        }
        final right = stack.removeLast();
        final left = stack.removeLast();

        switch (token) {
          case '+':
            stack.add(left + right);
            break;
          case '-':
            stack.add(left - right);
            break;
          case '*':
            stack.add(left * right);
            break;
          case '/':
            if (right == 0) {
              throw FormatException('Division by zero');
            }
            stack.add(left / right);
            break;
          case '%':
            stack.add(left % right);
            break;
          case '^':
            stack.add(math.pow(left, right).toDouble());
            break;
          default:
            throw FormatException('Unknown operator: $token');
        }
      }
    }

    if (stack.length != 1) {
      throw FormatException('Invalid expression');
    }

    return stack.single;
  }
}
