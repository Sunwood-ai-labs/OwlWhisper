import streamlit as st
import streamlit.components.v1 as components
import base64

def main():
    st.title("音声録音アプリ")

    # 録音ボタンを表示
    components.html("""
<button id="recordButton">録音開始</button>
<script>
let recorder;
let recordedChunks = [];

const recordButton = document.getElementById('recordButton');

recordButton.addEventListener('click', () => {
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        recordButton.textContent = '録音開始';
    } else {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                recorder = new MediaRecorder(stream);
                recorder.start();
                recordButton.textContent = '録音停止';

                recorder.addEventListener('dataavailable', event => {
                    if (event.data.size > 0) {
                        recordedChunks.push(event.data);
                    }
                });

                recorder.addEventListener('stop', () => {
                    const blob = new Blob(recordedChunks, { type: 'audio/webm' });
                    recordedChunks = [];

                    // 録音データをPythonに渡す
                    const reader = new FileReader();
                    reader.onload = () => {
                        const base64data = reader.result.split(',')[1];
                        window.parent.postMessage({ event: 'recordingComplete', data: base64data }, '*');
                    };
                    reader.readAsDataURL(blob);
                });
            });
    }
});
</script>
    """, height=50)

    # JavaScriptから録音データを受け取る
    if st.session_state.get('audio_data'):
        audio_data = st.session_state['audio_data']
        del st.session_state['audio_data']

        # 録音データをデコード
        audio_bytes = base64.b64decode(audio_data.split(',')[1])

        st.success("録音完了")
        
        # 録音データを再生するためのオーディオプレーヤーを表示
        st.audio(audio_bytes, format='audio/webm')

# JavaScriptからのメッセージを受け取るコールバック関数
def message_callback(event):
    if event.data.get('event') == 'recordingComplete':
        st.session_state['audio_data'] = event.data['data']
        st.experimental_rerun()

if __name__ == "__main__":
    main()