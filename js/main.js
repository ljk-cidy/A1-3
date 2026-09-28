// HTML에서 요소들 찾아오기
const aiInput = document.getElementById('ai-input');
const aiBtn = document.getElementById('ai-btn');
const resultText = document.getElementById('result-text');
const loadingSpinner = document.getElementById('loading-spinner');

// 버튼 클릭 시 이벤트 실행
aiBtn.addEventListener('click', () => {
    const inputValue = aiInput.value.trim();

    // 1. 입력값이 없을 때 alert 창 띄우기
    if (inputValue === "") {
        alert("내용을 입력해주세요!");
        aiInput.focus();
        return; // 아래 코드를 실행하지 않고 멈춤
    }

    // 2. 로딩 상태 시작 (버튼 비활성화, 스피너 표시)
    aiBtn.disabled = true;
    aiBtn.innerText = "로딩 중...";
    resultText.innerText = "AI가 열심히 답변을 준비하고 있습니다...";
    loadingSpinner.classList.remove('hidden'); // 스피너 보이기

    // 3. 임시 로딩 시뮬레이션 (약 2초 후 결과 표시)
    // ※ 추후 백엔드(Python) 연동 시 이 부분을 fetch('/api/...')로 바꿀 예정입니다.
    setTimeout(() => {
        // 결과 표시 및 로딩 상태 종료
        loadingSpinner.classList.add('hidden'); // 스피너 숨기기
        resultText.innerHTML = `<strong>'${inputValue}'</strong>에 대한 AI의 추천 결과입니다.<br><br>(여기에 진짜 AI 답변이 들어갑니다!)`;
        
        // 버튼 원래대로 복구
        aiBtn.disabled = false;
        aiBtn.innerText = "추천받기";
    }, 2000);
});