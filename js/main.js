document.addEventListener('DOMContentLoaded', () => {
    const aiInput = document.getElementById('ai-input');
    const aiBtn = document.getElementById('ai-btn');
    const resultText = document.getElementById('result-text');
    const loadingSpinner = document.getElementById('loading-spinner');

    if (!aiBtn || !aiInput) return;

    aiBtn.addEventListener('click', async () => {
        const inputValue = aiInput.value.trim();

        // 1. 빈 값 처리
        if (inputValue === "") {
            alert("내용을 입력해주세요!");
            aiInput.focus();
            return;
        }

        // 2. 로딩 상태 시작
        aiBtn.disabled = true;
        aiBtn.innerText = "생성 중...";
        resultText.innerText = "AI가 답변을 생각하는 중입니다...";
        if (loadingSpinner) loadingSpinner.classList.remove('hidden');

        try {
            // 3. 백엔드 API 호출
            const response = await fetch('/api/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputValue })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || `서버 오류 (${response.status})`);
            }

            // 4. 성공 결과 출력
            resultText.innerText = data.result;

        } catch (error) {
            console.error("AI 호출 에러:", error);
            resultText.innerText = `오류 발생: ${error.message}`;
        } finally {
            // 5. 로딩 상태 종료
            aiBtn.disabled = false;
            aiBtn.innerText = "추천받기";
            if (loadingSpinner) loadingSpinner.classList.add('hidden');
        }
    });
});