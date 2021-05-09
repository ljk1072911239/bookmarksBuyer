import 'package:flutter/material.dart';

void main() {
  runApp((MaterialApp(
    home: TelaPrincipal(),
    theme: new ThemeData(
      primaryColor: Colors.black,
      accentColor: Colors.black,
      primaryColorLight: Colors.black,
      textSelectionHandleColor: Colors.black,
      textSelectionColor: Colors.white,
    ),
  )));
}

class TelaPrincipal extends StatefulWidget {
  @override
  _TelaPrincipalState createState() => _TelaPrincipalState();
}

class _TelaPrincipalState extends State<TelaPrincipal> {
  TextEditingController _controllerStakeApostada = TextEditingController();
  TextEditingController _controllerOdd = TextEditingController();
  // TextEditingController _controllerLucroMinimo = TextEditingController();
  String _resultadoOdd = '-';
  String _resultadoStake = '-';

  void _calculos(){
    double _stakeApostada = double.parse(_controllerStakeApostada.text.replaceAll(',', '.'));
    double _oddApostada = double.parse(_controllerOdd.text.replaceAll(',', '.'));
    double _lucroMinimoP = (_porcentagemInteiro+(_porcentagemDecimal/10))/100;

    double _receitaApostada = num.parse((_stakeApostada*_oddApostada).toStringAsFixed(2));
    double _lucroMinimoR = _receitaApostada*_lucroMinimoP;
    _resultadoStake = (num.parse((_receitaApostada - _lucroMinimoR - _stakeApostada).toStringAsFixed(2))).toString();
    _resultadoOdd = (num.parse((_receitaApostada/double.parse(_resultadoStake)).toStringAsFixed(2))).toString();

    setState(() {
      _resultadoStake = (num.parse((_receitaApostada - _lucroMinimoR - _stakeApostada).toStringAsFixed(2))).toString();
      _resultadoOdd = (num.parse((_receitaApostada/double.parse(_resultadoStake)).toStringAsFixed(2))).toString();
    });
  }

  void _limparCampos(){
    _controllerStakeApostada.text = '';
    _controllerOdd.text = '';
    _porcentagemInteiro = 0;
    _porcentagemDecimal = 0;
    setState(() {
      _resultadoStake = '-';
      _resultadoOdd = '-';
    });
  }

  double _porcentagemInteiro = 0;
  double  _porcentagemDecimal = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Be Sure', style: TextStyle(color: Color(0xffdaa520 ), fontWeight: FontWeight.bold, fontSize: 25),),
        backgroundColor: Color(0xffba4a22),
      ),
      body: Container(
        color: Color(0xffc0c0c0),
        child: Padding(
          padding: EdgeInsets.all(32),
          child: Container(
              alignment: Alignment.center,
              child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: <Widget>[
                    Center(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Row(
                              children: [
                                Text('Odd: ', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                                Text(_resultadoOdd, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                              ],
                            ),
                            Row(
                              children: [
                                Text('Stake: \$', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                                Text(_resultadoStake, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold))
                              ],
                            )
                          ],
                        )
                    ),
                    TextField(
                        cursorColor: Colors.black,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(labelText: 'Stake Apostada'),
                        style: TextStyle(fontSize: 20, color: Colors.black,),
                        controller: _controllerStakeApostada,
                        onChanged: (text){
                          _calculos();
                        }
                    ),
                    TextField(
                        cursorColor: Colors.black,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(labelText: 'Odd Apostada'),
                        style: TextStyle(fontSize: 20, color: Colors.black),
                        controller: _controllerOdd,
                        onChanged: (text){
                          _calculos();
                        }
                    ),
                    Column(
                      children: [
                        Padding(
                          padding: const EdgeInsets.only(bottom: 10),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text('Lucro mínimo: ', style: TextStyle(fontSize: 20, color: Colors.black),),
                              Text(_porcentagemInteiro.toInt().toString()+'.'+_porcentagemDecimal.toInt().toString(), style: TextStyle(fontSize: 20, color: Colors.black),)
                            ],
                          ),
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('Inteiro:', style: TextStyle(fontSize: 15, color: Colors.black),),
                            SliderTheme(
                              child: Slider(
                                  value: _porcentagemInteiro,
                                  min: -10,
                                  max: 10,
                                  label: _porcentagemInteiro.toInt().toString(),
                                  divisions: 20,
                                  activeColor: Color(0xffba4a22),
                                  inactiveColor: Colors.black,
                                  onChanged: (double escolha){setState(() {
                                    _porcentagemInteiro = escolha;
                                    try {
                                      _calculos();
                                    }
                                    on Exception catch(_){
                                    }
                                  });},
                              ),
                              data: SliderTheme.of(context).copyWith(
                                  trackHeight: 28,
                                  thumbColor: Colors.transparent,
                                  thumbShape: RoundSliderThumbShape(enabledThumbRadius: 0.0)),
                            ),
                          ],
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('Decimal:', style: TextStyle(fontSize: 15, color: Colors.black),),
                            SliderTheme(
                              child: Slider(
                                value: _porcentagemDecimal,
                                min: 0,
                                max: 9,
                                label: _porcentagemDecimal.toInt().toString(),
                                divisions: 20,
                                activeColor: Color(0xffba4a22),
                                inactiveColor: Colors.black,
                                onChanged: (double escolha){setState(() {
                                  _porcentagemDecimal = escolha;
                                  try {
                                    _calculos();
                                  }
                                  on Exception catch(_){
                                  }
                                });},
                              ),
                              data: SliderTheme.of(context).copyWith(
                                  trackHeight: 28,
                                  thumbColor: Colors.transparent,
                                  thumbShape: RoundSliderThumbShape(enabledThumbRadius: 0.0)),
                            ),
                          ],
                        ),
                      ],
                    ),
                    Column(
                      children: [
                        SizedBox(
                          width: double.infinity,
                          child: RaisedButton(
                              child: Text('Limpar',
                                  style: TextStyle(
                                      color: Color(0xffdaa520),
                                      fontSize: 20,
                                      fontWeight: FontWeight.bold
                                  )
                              ),
                              color: Color(0xffba4a22),
                              onPressed: () => {_limparCampos()}),
                        ),
                      ],
                    ),
                  ]
              )
          )
          ),
      ),
    );
  }
}
