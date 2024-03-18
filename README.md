<h1>
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/OwlWhisper/main/docs/OwlWhisper.png" height=200px align="left"/>
OwlWhisper <br>
</h1>


OwlWhisperは、高速な音声認識ライブラリ「Faster Whisper」と、高品質な音声合成ライブラリ「Style-Bert-VITS2」を組み合わせたプロジェクトです。初心者でも簡単に音声認識と音声合成を体験できるように設計されています。

## 特徴

- WSL2、Docker、Streamlit、FastAPI、PyTorch、CUDA、Style-Bert-VITS2、Faster Whisperを使用した最新の技術スタック
- Webカメラを使った音声認識APIの提供
- 音声対話型のチャットボット機能

![](https://github.com/Sunwood-ai-labs/OwlWhisper/blob/main/docs/demo.gif?raw=true)


## 必要な環境

- Windows 10以降のOS
- WSL2 (Windows Subsystem for Linux 2)
- Docker
- NVIDIA GPUとCUDAドライバー

## セットアップ

1. このリポジトリをクローンします。
2. WSL2とDockerをインストールし、設定します。
3. NVIDIA GPUとCUDAドライバーを正しくインストールします。
4. .envファイルの設定(`.env.example`を参考にしてください)

```bash

GOOGLE_AI_STUDIO_API_KEY=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
CAMERA_URL=http://host.docker.internal:8100/camera
FAST_WISPER_API_URL=http://fast-wisper-api:8181/transcribe
STYLE_BERT_VITS2_API_URL=http://style-bert-vits2-api:5000/voice

```

## Webカメラ API の起動方法

1. コマンドプロンプトを開きます。
2. プロジェクトのルートディレクトリに移動します。
3. 以下のコマンドを実行します：

```bash
C:\Prj\OwlWhisper>camera-api.bat
```

4. Anacondaの仮想環境 "yva" がアクティベートされ、Webカメラ APIが起動します。

## チャットボットの起動方法

1. WSL2のターミナルを開きます。
2. プロジェクトのルートディレクトリに移動します。
3. 以下のコマンドを実行します：

```bash
maki@TurtleTower:/mnt/c/Prj/OwlWhisper$ docker-compose up
```

4. Docker Composeが各サービス（Style-Bert-VITS2 API、Faster Whisper API、Streamlitアプリケーション）を起動します。

## 使い方


### Chatbotの起動

- Webカメラ APIは、`http://localhost:8100` でアクセスできます。
- チャットボットは、Streamlitアプリケーションとして `http://localhost:8502` で利用できます。


![alt text](docs\image.png)

### キャラクターの描画

Vtude Studioでキャラクターを描画してOBS Studio等で重ねてください
![alt text](docs\image2.png)