# Decision-Grade Data Science

**모호한 질문과 엉킨 데이터에서 시작해, 검증되고 재현 가능한 의사결정을 지향하는 데이터 분석·머신러닝·AI 모델링용 오픈소스 에이전트 스킬입니다.**

[English](README.md) · [방법론](docs/methodology.md) · [평가 방식](docs/evaluation.md) · [기여 안내](CONTRIBUTING.md)

[![Decision-Grade Data Science — 엉킨 데이터를 방어 가능한 의사결정으로.](docs/assets/social-card.svg)](docs/methodology.md)

*엉킨 데이터를 방어 가능한 의사결정으로 — [근거 중심 방법론 보기](docs/methodology.md).*

Decision-Grade Data Science는 에이전트가 분석 코드를 빨리 만드는 데서 멈추지 않고, 실제 의사결정과 그 결정을 뒷받침하는 근거의 연결을 보존하도록 만듭니다.

## 왜 필요한가

AI 에이전트는 잘못된 분석 단위를 선택하거나, 편리한 컬럼을 정답으로 믿거나, 미래 정보를 누수하거나, 결과를 본 뒤 평가 기준을 바꾸거나, 한 번 성공한 실행만으로 완료를 선언할 수 있습니다.

이 스킬 모음은 다음 흐름을 적용합니다.

    의사결정 계약
      → 데이터와 정답 감사
      → 누수 없는 기준선
      → 통제 실험
      → 독립 검증
      → 실패 원인 진단
      → 클린 실행 재현과 인수인계

## 포함된 스킬

| 스킬 | 사용 목적 |
|---|---|
| [Run Decision-Grade Data Science](skills/running-decision-grade-data-science/SKILL.md) | 모호하거나 여러 단계에 걸친 데이터 사이언스 프로젝트 총괄 |
| [Audit Data and Ground Truth](skills/auditing-data-and-ground-truth/SKILL.md) | 분석 단위, 조인, 시간 의미, 결측, 라벨, 정본 신뢰성 감사 |
| [Design Leakage-Safe Experiments](skills/designing-leakage-safe-experiments/SKILL.md) | 예측 시점, 분할, 기준선, 지표와 공정한 비교 설계 |
| [Validate Models and Claims](skills/validating-models-and-claims/SKILL.md) | 모델과 분석 주장을 독립 근거로 검증 |
| [Diagnose ML Failures](skills/diagnosing-ml-failures/SKILL.md) | 데이터부터 런타임까지 성능 하락과 불일치의 최초 고장 계층 격리 |
| [Ship Reproducible Results](skills/shipping-reproducible-results/SKILL.md) | 실행 이력, 재현 증거, 한계와 소유권을 포함한 인수인계 |

전체 프로젝트에는 첫 번째 스킬을, 특정 문제에는 목적이 가장 가까운 전문 스킬을 사용합니다.

## 설치

설치 전에 제3자 스킬의 내용을 검토하세요.

GitHub CLI에서 gh skill을 지원하는 버전을 사용하는 경우:

    gh skill preview aiopshwang/data-analysis-ml-agent-skills
    gh skill install aiopshwang/data-analysis-ml-agent-skills running-decision-grade-data-science --agent codex

Agent Skills CLI로 Codex에 전체 스킬을 설치하는 경우:

    npx skills add aiopshwang/data-analysis-ml-agent-skills --skill '*' --global --agent codex --copy --yes

Claude Code에는 codex 대신 claude-code를 사용합니다. 직접 설치하려면 저장소를 clone한 뒤 원하는 skill 디렉터리를 에이전트의 사용자 또는 프로젝트 skill 경로로 복사할 수 있습니다.

## 사용 예

    Use $running-decision-grade-data-science to turn this request into a decision-ready, reproducible project.

    Use $auditing-data-and-ground-truth to audit these tables and labels before modeling.

    Use $validating-models-and-claims to check whether the evidence supports this launch claim.

## 핵심 원칙

- 모델보다 의사결정, 분석 단위, 목표와 시간 경계를 먼저 고정합니다.
- 원본 입력을 보존하고 모든 파생 데이터가 원천으로 추적되게 합니다.
- 정답도 감사 대상이며, 사람이 최종 판단권을 갖습니다.
- 단순한 기준선에서 시작하고 측정된 개선만 복잡도를 정당화합니다.
- 실패와 기각 실험도 보존합니다.
- 주장과 같은 범위의 근거가 있을 때만 완료를 선언합니다.
- 재현 절차와 한계를 최종 산출물의 일부로 취급합니다.

## 범위와 한계

이 프로젝트는 AutoML 프레임워크나 도메인 전문가의 대체물이 아닙니다. 모든 작업에 모든 단계를 강제하지 않으며, 에이전트에 비공개 데이터 접근·비용 발생·배포·외부 공개 권한을 부여하지 않습니다. 모델 성능, 공정성, 안전성 또는 규제 준수를 보장하지도 않습니다.

## 검증

    python -m pip install -r requirements-dev.txt
    python scripts/validate_repo.py
    python scripts/scan_public.py
    pytest

저장소는 스킬과 플러그인 메타데이터, 로컬 링크, 미완성 문구, 트리거 평가셋, 비밀정보 패턴을 검사합니다. 정적 검사와 별도로 독립적인 행동 평가도 수행합니다.

## aiopshwang 스킬 패밀리

함께 쓰기 좋은 독립 Agent Skill들:

- [goal-to-proof](https://github.com/aiopshwang/goal-to-proof) — 범용 완료 게이트: 승인된 작업을 끝까지 수행하고 결과를 증명합니다.
- [verify-regression-tests](https://github.com/aiopshwang/verify-regression-tests) — 회귀 테스트가 의도한 결함을 실제로 잡는지 증명합니다.
- [ship-mobile-app](https://github.com/aiopshwang/ship-mobile-app) — 도메인·상태·라이프사이클·플랫폼·릴리스 경계를 관통하는 프로덕션 모바일 작업을 다룹니다.

## 개인정보와 라이선스

공개 저장소에는 일반화된 절차와 합성 템플릿만 포함하며 고객 데이터나 기존 프로젝트 원문을 포함하지 않습니다. 보안 제보 방법과 신뢰 경계는 [SECURITY.md](SECURITY.md)를 확인하세요.

[MIT License](LICENSE)
