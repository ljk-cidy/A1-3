document.addEventListener('DOMContentLoaded', () => {
    const aiInput = document.getElementById('ai-input');
    const aiBtn = document.getElementById('ai-btn');
    const resultText = document.getElementById('result-text');
    const loadingSpinner = document.getElementById('loading-spinner');

    if (!aiBtn || !aiInput) return;

    aiBtn.addEventListener('click', async () => {
        const inputValue = aiInput.value.trim();

        if (inputValue === "") {
            alert("내용을 입력해주세요!");
            aiInput.focus();
            return;
        }

        aiBtn.disabled = true;
        aiBtn.innerText = "생성 중...";
        resultText.innerText = "AI가 답변을 생각하는 중입니다...";
        if (loadingSpinner) loadingSpinner.classList.remove('hidden');

        try {
            const response = await fetch('/api/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: inputValue })
            });

            let data = {};
            try {
                data = await response.json();
            } catch {
                // JSON이 아닌 응답이면 무시하고 아래에서 상태 코드로 처리
            }

            if (!response.ok) {
                throw new Error(data.error || `서버 오류 (${response.status})`);
            }

            resultText.innerText = data.result ?? "응답에 결과가 없습니다.";

        } catch (error) {
            console.error("AI 호출 에러:", error);
            resultText.innerText = `오류 발생: ${error.message}`;
        } finally {
            aiBtn.disabled = false;
            aiBtn.innerText = "추천받기";
            if (loadingSpinner) loadingSpinner.classList.add('hidden');
        }
    });
});