document.addEventListener('DOMContentLoaded', () => {
    const aiInput = document.getElementById('ai-input');
    const aiBtn = document.getElementById('ai-btn');
    const resultText = document.getElementById('result-text');
    const loadingSpinner = document.getElementById('loading-spinner');

    // 기획서 기준 안내 문구
    const MSG_EMPTY = "재료를 1개 이상 입력해주세요.";
    const MSG_LOADING = "AI가 레시피를 생각 중입니다...";
    const MSG_FAIL = "서버 연결에 실패했습니다. 잠시 후 다시 시도해주세요.";
    const COOLDOWN_MS = 3000; // 연속 클릭 방지 (요청 후 3초간 버튼 비활성화)

    if (!aiBtn || !aiInput) return;

    aiBtn.addEventListener('click', async () => {
        const inputValue = aiInput.value.trim();

        if (inputValue === "") {
            alert(MSG_EMPTY);
            aiInput.focus();
            return;
        }

        aiBtn.disabled = true;
        aiBtn.innerText = "생성 중...";
        resultText.classList.remove('recipe');
        resultText.innerText = MSG_LOADING;
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
                const err = new Error(data.error || `서버 오류 (${response.status})`);
                err.status = response.status;
                throw err;
            }

            resultText.innerText = data.result ?? "응답에 결과가 없습니다.";
            resultText.classList.add('recipe');

        } catch (error) {
            console.error("AI 호출 에러:", error);
            // 입력 문제(400)는 서버 안내를 그대로, 그 외는 기획서 문구로 표시
            resultText.innerText = error.status === 400 ? error.message : MSG_FAIL;
        } finally {
            aiBtn.innerText = "추천받기";
            if (loadingSpinner) loadingSpinner.classList.add('hidden');
            setTimeout(() => { aiBtn.disabled = false; }, COOLDOWN_MS);
        }
    });
});