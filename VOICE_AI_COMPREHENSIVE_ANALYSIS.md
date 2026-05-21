# Voice AI Bot Performance Analysis - The Derma Co
**Analysis Date:** May 21, 2026  
**Period Analyzed:** May 19-21, 2026 (3 days)  
**Total Calls:** 3,331  
**Total Conversation Time:** 113.7 hours

---

## 🎯 EXECUTIVE SUMMARY & RECOMMENDATION

### The Bottom Line: **Scale with Significant Improvements Needed**

The voice AI bot is handling a large volume of calls (3,331 in 3 days) and is preventing 84% of calls from reaching human agents. However, **it's not actually resolving most customer issues**, which is a critical problem. The bot should be scaled cautiously while addressing core performance gaps.

**Verdict:** ⚠️ **YES, scale to other brands, BUT only after fixing the resolution quality issues.** Current performance could damage brand reputation if scaled without improvements.

---

## 1️⃣ CUSTOMER SATISFACTION (CSAT) - **CRITICAL ISSUE**

### Key Metrics:
- **Average CSAT:** 3.05/5 (out of 5)
- **CSAT Responses:** 1,108 calls (33.3% of total)
- **Satisfied (4-5 stars):** 366 customers (33.0%)
- **Neutral (3 stars):** 311 customers (28.1%)
- **Dissatisfied (1-2 stars):** 431 customers (38.9%) ❌

### What This Means:
- **Nearly 40% of customers are unhappy** with the bot interaction
- Only 1 in 3 customers are satisfied
- The bot is creating more frustrated customers than happy ones
- **This is a scaling risk** - if you roll this out to 10x calls, you'll have 10x unhappy customers

### CSAT Distribution:
```
2-star (Most common):  359 responses (32.4%)
3-star:                311 responses (28.1%)
1-star:                 72 responses (6.5%)
4-star:                176 responses (15.9%)
5-star:                190 responses (17.1%)
```

---

## 2️⃣ RESOLUTION SUCCESS - **MAJOR RED FLAG**

### The Reality:
| Status | Count | % | Assessment |
|--------|-------|---|------------|
| **Transferred to Human** | 532 | 16.0% | Bot gave up, escalated |
| **Resolved by Bot** | 367 | 11.0% | ✓ Actually helped |
| **Abandoned by User** | 233 | 7.0% | Customer left frustrated |
| **Unknown** | 5 | 0.2% | Missing data |

### The Problem:
- **Only 11% of calls were actually resolved by the bot** (367 out of 3,331)
- 2,222 calls (66.7%) were NOT resolved by the bot
- The bot is handling calls but **not solving problems**
- This suggests customers are leaving without answers

---

## 3️⃣ ESCALATION TO HUMAN SUPPORT - **BOTTLENECK ANALYSIS**

### Escalation Rate:
- **Transferred to Human:** 532 calls (16%)
- **Handled Entirely by Bot:** 2,799 calls (84%)

### Why Customers Are Being Escalated (of those transferred):
1. **Policy restriction (Human required):** 307 calls (57.7%)
   - Bot correctly identifies these can't be resolved automatically (refunds, complex returns, etc.)
   
2. **Requested by User:** 140 calls (26.3%)
   - Customer explicitly asked to speak to a human
   - **Sign:** Customer doesn't trust the bot to solve their problem
   
3. **Bot failed to understand:** 73 calls (13.7%)
   - Speech recognition issues, language barriers
   - Customer had to repeat themselves multiple times

### Key Insight:
**84% of calls never reach a human, but only 11% are actually resolved.** This means the bot is:
- ✅ Avoiding unnecessary escalations (good)
- ❌ But leaving customers without solutions (bad)

---

## 4️⃣ CUSTOMER ISSUES - WHAT CUSTOMERS ACTUALLY NEED HELP WITH

### Top Issues (with 55 unique categories):

| Issue | Count | % | Severity |
|-------|-------|---|----------|
| **Shipping Delay** | 278 | 8.3% | 🔴 Highest |
| **Order Tracking** | 207 | 6.2% | 🟡 High |
| **Other** | 139 | 4.2% | 🔴 Unclear |
| **Refund** | 111 | 3.3% | 🔴 High |
| **Missing Item** | 103 | 3.1% | 🔴 High |
| **Missing Items** | 91 | 2.7% | 🔴 High |
| **Cancellation** | 80 | 2.4% | 🟡 Medium |
| **Wrong Item** | 68 | 2.0% | 🔴 High |

### Analysis:
**55 different issue categories** = The bot is facing a complex problem space

**Top 3 Problems (25.7% of all calls):**
1. **Shipping/Fulfillment Issues** (Shipping Delay, Order Tracking, Missing Items, Wrong Item) = **~750 calls**
2. **Refund/Return Issues** = **~200+ calls**
3. **General/Unclear Issues** = **139 calls**

### Bot Performance by Issue Category:

**High Effectiveness (Quickly Resolved):**
- None specifically flagged as high
- Only 2 calls labeled "High (Solved issue quickly)"

**Medium Effectiveness (17.1% of calls):**
- 569 calls rated medium effectiveness
- Bot provides some help but not complete resolution

**Low Effectiveness (6.4% of calls):**
- 214 calls rated low effectiveness
- Bot fails to help or understand

---

## 5️⃣ WHERE THE VOICE AI IS LAGGING - PERFORMANCE GAPS

### Critical Failure Areas:

#### 🔴 **Problem 1: Refund Timeline & Policy Clarity**
- Customers don't understand when refunds will arrive
- Bot gives generic responses, not customer-specific timelines
- Friction point mentioned frequently: "Bot did not provide clear refund timeline"
- **Fix needed:** Access to real refund processing data, ability to provide ETA

#### 🔴 **Problem 2: Shipping/Delivery Tracking**
- 278 shipping delay complaints = 8.3% of ALL calls
- Customers ask "where is my order?" and bot has no update
- Friction point: "Bot did not provide resolution or update on rescheduled delivery"
- **Fix needed:** Real-time integration with shipping carriers, delivery agent communication

#### 🔴 **Problem 3: Language & Speech Recognition Issues**
- Bot struggles with customer speech: "Bot misunderstood 'Mercedes Guardia Lavaluna'"
- Language mixing and code-switching causes failures
- Multiple clarification attempts needed
- **Fix needed:** Better speech-to-text model, multilingual support, accent tolerance

#### 🔴 **Problem 4: Missing Items & Wrong Orders**
- 194 calls about missing/wrong items (5.8% of total)
- These require manual investigation - bot can't resolve
- **Fix needed:** Can't be fully automated; always needs human follow-up

#### 🔴 **Problem 5: Customer Frustration Detection**
- Friction points show repeated mentions of "frustration," "frustrated," "escalate"
- Bot doesn't detect frustration and switch to human proactively
- **Fix needed:** Add sentiment analysis, automatic escalation when customer is upset

#### 🟡 **Problem 6: "Unknown" Issues (3,192 calls in "Unknown" category)**
- This is concerning - many calls have issues labeled "Unknown"
- Bot may not be correctly categorizing what customers need
- **Fix needed:** Better issue classification, more training examples

### Summary of Bot Effectiveness:
- **10.1%:** High effectiveness (338 calls)
- **17.1%:** Medium effectiveness (569 calls)
- **6.4%:** Low effectiveness (214 calls)
- **66.3%:** Unknown/not resolved (2,210 calls)

**Only about 27% of calls have Medium or High effectiveness rating.**

---

## 6️⃣ GENERAL TRENDS OF THE CALLS

### Daily Volume & Patterns:
- **May 19:** ~1,100 calls/day
- **May 20:** ~1,100 calls/day
- **May 21:** ~1,100 calls/day
- **Pattern:** Consistent volume across all 3 days (steady-state operation)

### Call Duration:
- **Average:** 122.9 seconds (~2 minutes)
- **Total volume:** 113.7 hours in 3 days
- **This is efficient** in terms of time spent per call

### Key Trend Insight:
The bot is consistently handling ~1,100 calls/day with ~2min average duration. It's a high-volume, brief interaction system. However, the **brevity may be the problem** - customers aren't getting their issues resolved in 2 minutes.

---

## 📊 VOICE AI BOT EFFECTIVENESS VERDICT

### What's Working ✅
1. **Volume handling:** Bot manages 1,100+ calls/day without human intervention
2. **Efficiency:** Average 2-minute calls, 16% escalation rate
3. **Policy recognition:** Bot correctly identifies when human is required (57.7% of transfers)
4. **Some resolution:** 11% of calls genuinely resolved

### What's Broken ❌
1. **Low CSAT:** 3.05/5 = Customers are unhappy (38.9% dissatisfied)
2. **Low resolution rate:** Only 11% actually resolved
3. **High abandonment:** 7% of customers give up mid-call
4. **Shipping/tracking:** Can't access real-time data (278 calls)
5. **Speech recognition:** Struggles with accents, speech clarity, language mixing
6. **Frustration handling:** No escalation when customer is upset
7. **Issue complexity:** 55 different issue types - system is too rigid

---

## 🚀 SHOULD YOU SCALE TO OTHER BRANDS?

### The Answer: **YES, BUT WITH CONDITIONS**

### Recommendation: **Scale with a 2-Phase Approach**

#### **Phase 1: Fix & Improve (Weeks 1-4)**
Before scaling, fix these critical issues:

1. **Integrate Real-Time Data** (Priority: CRITICAL)
   - Order status API
   - Shipping/tracking integration
   - Refund processing timeline
   - *Impact:* This alone could improve resolution rate from 11% to 40%

2. **Improve Speech Recognition** (Priority: HIGH)
   - Better language detection
   - Regional accent training
   - Code-switching tolerance
   - *Impact:* Reduce "bot failed to understand" from 13.7% to <5%

3. **Add Sentiment Analysis** (Priority: HIGH)
   - Detect frustration in customer speech
   - Automatic escalation when CSAT would be <3
   - *Impact:* Prevent unhappy customers from staying on bot

4. **Improve Issue Classification** (Priority: MEDIUM)
   - Train on "Unknown" category (3,192 calls)
   - Create decision trees for complex issues
   - *Impact:* Better route to resolution or escalation

5. **Customer-Specific Solutions** (Priority: MEDIUM)
   - Provide personalized refund timelines (not generic)
   - Real-time shipping updates (not "your order is being processed")
   - Order-specific status (not template responses)

#### **Phase 2: Scale Rollout (Weeks 5+)**
After improvements:

- **Start with similar category brands** (derma/health, beauty, fashion)
- Target brands with similar issue types (order, shipping, refund)
- **Avoid** brands with complex/custom issues (luxury goods, cars, complex services)
- Monitor CSAT on new brands - should target >3.5/5 before full rollout

### Success Metrics to Track:
| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| CSAT | 3.05 | 3.75+ | 4 weeks |
| Resolution Rate | 11% | 35%+ | 4 weeks |
| Escalation Rate | 16% | 10% | 4 weeks |
| Customer Satisfaction (4-5 stars) | 33% | 50%+ | 4 weeks |

---

## 🎬 IMMEDIATE ACTION ITEMS

### Quick Wins (Do First):
1. **Add Sentiment Analysis** - Detect "frustrated," "angry," and auto-escalate
2. **Integrate Shipping API** - Give real tracking updates instead of generic responses
3. **Test on New Brand** - Pick a similar brand, run in beta
4. **Improve Speech Recognition** - Focus on regional accents and language mixing

### Medium-Term (Weeks 2-4):
1. Fix refund timeline integration
2. Improve issue classification accuracy
3. A/B test sentiment-based escalation
4. Gather feedback from beta brand

### Long-Term (Month 2+):
1. Expand to 3-5 new brands
2. Build brand-specific training data
3. Monitor CSAT trends weekly
4. Quarterly optimization sprints

---

## 📋 FINAL SUMMARY TABLE

| Aspect | Rating | Status | Notes |
|--------|--------|--------|-------|
| **Customer Satisfaction** | 3.05/5 | 🔴 Poor | 38.9% dissatisfied, only 33% satisfied |
| **Resolution Success** | 11% | 🔴 Critical | 89% of calls unresolved by bot |
| **Escalation Logic** | 16% | 🟢 Good | Correctly escalates policy issues |
| **Volume Handling** | 1,100/day | 🟢 Good | Consistent, efficient throughput |
| **Issue Coverage** | 55 types | 🟡 Complex | Too many edge cases, needs simplification |
| **Readiness to Scale** | Not Ready | 🔴 No | Fix CSAT & resolution first |

---

## ✅ CONCLUSION

**The voice AI bot is a volume handler, not a problem solver.** It's successfully:
- Handling 3,331 calls in 3 days
- Preventing unnecessary escalations (84% bot-handled)
- Running efficiently (2 min/call)

But it's **failing to actually help customers** - 89% of calls leave without resolution, CSAT is below average, and 38.9% of customers are dissatisfied.

**Scale to other brands YES, but:**
1. First invest 4 weeks in improving resolution quality
2. Target 35%+ resolution rate and 3.75+ CSAT before scaling
3. Start with 1-2 pilot brands before going to 10+
4. Focus on data integration (shipping, refunds) as quick win

The infrastructure and volume handling are solid. The problem-solving capability needs work. Fix that first, then scale.
