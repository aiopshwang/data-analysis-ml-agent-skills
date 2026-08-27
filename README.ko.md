# Decision-Grade Data Science

**모호한 질문과 엉킨 데이터에서 시작해, 검증되고 재현 가능한 의사결정에 도달하는 데이터 분석·머신러닝·AI 모델링용 오픈소스 에이전트 스킬입니다.**

[English](README.md) · [방법론](docs/methodology.md) · [평가 방식](docs/evaluation.md) · [기여 안내](CONTRIBUTING.md)

[![Decision-Grade Data Science — 엉킨 데이터를 방어 가능한 의사결정으로.](docs/assets/social-card.svg)](docs/methodology.md)

*엉킨 데이터를 방어 가능한 의사결정으로 — [근거 중심 방법론 보기](docs/methodology.md).*

라우터 하나, 라이프사이클 오케스트레이터 하나, 전문 스킬 다섯 개 — 총 일곱 개의 스킬이 코딩 에이전트가 실제 의사결정과 그것을 뒷받침하는 근거의 연결을 보존하도록 가르칩니다. 잘 꾸민 노트북이나 높은 검증 점수만으로는 부족한 작업을 위해 만들었습니다.

## 왜 필요한가

AI 에이전트는 분석 코드를 빠르게 작성합니다. 그러나 잘못된 행 단위를 조용히 선택하고, 편리한 컬럼을 정답으로 믿고, 미래 정보를 누수하고, 결과를 본 뒤 평가 기준을 옮기고, 한 번 성공한 실행만으로 완료를 선언하기도 합니다.

이 스킬 모음은 사람이 통제하는 운영 규율을 더합니다.

    의사결정 계약
      → 데이터와 정답 감사
      → 누수 없는 기준선
      → 통제 실험
      → 독립 검증
      → 실패 원인 진단
      → 클린룸 재현과 인수인계

목표는 작업을 늦추는 것이 아닙니다. 검증을 건너뛰는 대신, 명확한 의사결정과 재사용 가능한 근거, 반증 가능한 점검에서 속도가 나오게 하는 것입니다.

## 포함된 스킬

라우터가 올바른 진입점을 고르고, 오케스트레이터가 전체 라이프사이클을 진행하며, 다섯 개의 전문 스킬이 각 단계를 담당합니다.

    using-data-analysis  (라우터 — 어떤 스킬이 맞는지 애매하면 여기서 시작)
      └─ running-decision-grade-data-science  (라이프사이클 오케스트레이션)
           1. auditing-data-and-ground-truth      — 데이터·정답 감사
           2. designing-leakage-safe-experiments  — 실험 설계
           3. validating-models-and-claims        — 검증
           4. diagnosing-ml-failures              — 실패 진단
           5. shipping-reproducible-results       — 재현 가능한 인수인계

| 스킬 | 사용 목적 |
|---|---|
| [Using Data Analysis Skills](skills/using-data-analysis/SKILL.md) — *진입점* | 데이터 분석·ML 요청을 가장 목적이 가까운 스킬로 라우팅 |
| [Run Decision-Grade Data Science](skills/running-decision-grade-data-science/SKILL.md) | 모호하거나 여러 단계에 걸친 데이터 사이언스 프로젝트 총괄 |
| [Audit Data and Ground Truth](skills/auditing-data-and-ground-truth/SKILL.md) | 분석 단위, 조인, 시간 의미, 결측, 라벨, 정본 신뢰성 감사 |
| [Design Leakage-Safe Experiments](skills/designing-leakage-safe-experiments/SKILL.md) | 예측 시점, 분할, 기준선, 지표와 공정한 비교 설계 |
| [Validate Models and Claims](skills/validating-models-and-claims/SKILL.md) | 모델과 분석 주장이 근거로 뒷받침되는 범위를 정확히 판정 |
| [Diagnose ML Failures](skills/diagnosing-ml-failures/SKILL.md) | 데이터부터 런타임까지 성능 하락과 불일치의 최초 고장 계층 격리 |
| [Ship Reproducible Results](skills/shipping-reproducible-results/SKILL.md) | 실행 이력, 재현 증거, 한계와 소유권을 포함한 인수인계 |

각 스킬은 핵심 지침, 더 깊은 참고 자료, 재사용 가능한 산출물 템플릿을 포함합니다. 전체 프로젝트에는 오케스트레이터를, 특정 문제에는 전문 스킬을 사용하고, 어느 스킬이 맞는지 애매할 때는 라우터가 대신 골라 줍니다.

## 설치

설치 전에 제3자 스킬의 내용을 검토하세요.

### GitHub CLI

gh skill 공개 프리뷰가 포함된 GitHub CLI 버전을 사용하는 경우:

    gh skill preview aiopshwang/data-analysis-ml-agent-skills
    gh skill install aiopshwang/data-analysis-ml-agent-skills running-decision-grade-data-science --agent codex

필요에 따라 스킬 이름이나 에이전트 호스트를 바꿔 사용합니다. GitHub CLI가 지원하는 호스트에는 Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI가 있습니다.

### Agent Skills CLI

Codex에 전체 스킬을 전역 설치하는 경우:

    npx skills add aiopshwang/data-analysis-ml-agent-skills --skill '*' --global --agent codex --copy --yes

Claude Code에는 codex 대신 claude-code를 사용합니다.

### 수동 설치

저장소를 clone하고 원하는 디렉터리를 검토한 뒤, 에이전트의 사용자 또는 프로젝트 skill 경로로 복사합니다.

    git clone https://github.com/aiopshwang/data-analysis-ml-agent-skills.git

저장소에는 Claude Code용 플러그인 매니페스트([.claude-plugin/plugin.json](.claude-plugin/plugin.json))와 Codex용 매니페스트([.codex-plugin/plugin.json](.codex-plugin/plugin.json))도 포함되어 있습니다.

## 사용 예

    Use $using-data-analysis to pick the right skill in this suite for my analysis task.

    Use $running-decision-grade-data-science to turn this vague churn-model request into a decision-ready project.

    Use $auditing-data-and-ground-truth to inspect these tables and labels before modeling.

    Use $designing-leakage-safe-experiments to create a fair grouped and temporal evaluation.

    Use $validating-models-and-claims to check whether this report supports the launch claim.

    Use $diagnosing-ml-failures to isolate the first broken layer behind this regression.

    Use $shipping-reproducible-results to prepare an independent clean-room handoff.

스킬은 기본적으로 암시적 선택을 허용하므로, 목적이 분명한 일반 요청만으로도 알맞은 스킬이 선택될 수 있습니다.

## 핵심 원칙

- 모델보다 의사결정, 분석 단위, 목표와 시간 경계를 먼저 고정합니다.
- 원본 입력을 보존하고 모든 파생 데이터가 원천으로 추적되게 합니다.
- 정답 라벨도 신뢰할 컬럼명이 아니라 감사할 근거로 취급합니다.
- 복잡도를 더하기 전에 투명한 기준선을 먼저 세웁니다.
- 한 번에 하나의 핵심 요인만 바꾸고, 실패한 실험도 보존합니다.
- 모든 주장을 같은 범위의 근거와 대응시킵니다.
- 모델의 판단, 결정론적 계산, 사람의 최종 판단권을 분리합니다.
- 부분 실행, 통과한 단위 테스트 하나, 성공한 예시 하나를 완료라고 부르지 않습니다.

전체 논리와 경계는 [방법론 문서](docs/methodology.md)에서 확인하세요.

## 범위와 한계

- AutoML 프레임워크가 아닙니다.
- 도메인 전문성이나 통계적 판단의 대체물이 아닙니다.
- 모든 분석에 모든 게이트가 필요하다는 뜻이 아닙니다.
- 에이전트에 비공개 데이터 접근, 비용 발생, 배포, 외부 공개 권한을 부여하지 않습니다.
- 모델 성능, 공정성, 안전성, 규제 준수를 보장하지 않습니다.

스킬은 의사결정 위험도에 맞게 깊이를 조절하고, 핵심 선택을 안전하게 추론할 수 없을 때만 사람의 입력을 요청합니다.

## 검증

저장소는 매니페스트와 프론트매터 무결성, 로컬 링크, UI 메타데이터, 미완성 문구, 트리거 평가셋 커버리지, 공개 콘텐츠의 비밀정보 패턴을 검사합니다.

    python -m pip install -r requirements-dev.txt
    python scripts/validate_repo.py
    python scripts/scan_public.py
    pytest

[트리거 프롬프트 세트](evals/trigger-prompts.yaml)는 일곱 개 스킬 전체에 대한 직접·간접·부정 사례를 포함합니다. 정적 검사가 행동을 증명하지는 않습니다. 독립 평가자가 합성 시나리오 하나를 수행한 기록은 [v0.1.0 독립 포워드 테스트 기록](evals/results/v0.1.0-forward-test.md)에서 확인할 수 있습니다.

## 개인정보와 보안

공개 저장소에는 일반화된 절차와 합성 템플릿만 포함하며 고객 데이터나 기존 프로젝트 원문을 포함하지 않습니다. 제품, 워크스페이스, 권한, 보존 정책이 적절하지 않다면 민감한 데이터를 에이전트에 붙여 넣지 마세요.

보안 제보 방법과 신뢰 경계는 [SECURITY.md](SECURITY.md)를 확인하세요.

## aiopshwang 스킬 패밀리

함께 쓰기 좋은 독립 Agent Skill들:

- [goal-to-proof](https://github.com/aiopshwang/goal-to-proof) — 범용 완료 게이트: 승인된 작업을 끝까지 수행하고 결과를 증명합니다.
- [verify-regression-tests](https://github.com/aiopshwang/verify-regression-tests) — 회귀 테스트가 의도한 결함을 실제로 잡는지 증명합니다.
- [ship-mobile-app](https://github.com/aiopshwang/ship-mobile-app) — 도메인·상태·라이프사이클·플랫폼·릴리스 경계를 관통하는 프로덕션 모바일 작업을 다룹니다.
- [fresh-eyes-check](https://github.com/aiopshwang/fresh-eyes-check) — 맥락 없는 다른 모델이 예전 지시가 지금도 맞는지 확인한 뒤 행동.

## 라이선스

[MIT](LICENSE)
