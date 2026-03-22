# Card System — Admin TODO

**Created:** 21 March 2026
**Status:** Pending

---

## 1. Interventions Subfolder Restructuring

The `interventions_*` cards in Element 2 are specifically about **AI-augmented** interventions but their filenames don't make this clear. They should be:

- **Renamed** from `interventions_[stage].md` → `ai_interventions_[stage].md`
- **Moved** into `cards/ai_augmented/` subfolder
- **H1 titles** changed from "AI Interventions:" → "AI-Augmented Interventions:"

Similarly, the `taxonomy_*` cards and cross-cutting cards should be moved into `cards/taxonomy/`.

### Target structure
```
cards/
├── _INDEX_interventions.md
├── ai_augmented/
│   ├── ai_interventions_discovery.md
│   ├── ai_interventions_define.md
│   ├── ai_interventions_ideate.md
│   ├── ai_interventions_prototype.md
│   ├── ai_interventions_test.md
│   ├── ai_interventions_cross_stage.md
│   └── QUICK_REF_failure_recovery.md
└── taxonomy/
    ├── taxonomy_discovery.md
    ├── taxonomy_define.md
    ├── taxonomy_ideate.md
    ├── taxonomy_prototype_test.md
    ├── assumption_mapping.md
    └── pattern_interrupts.md
```

### When moving:
- Update `source_doc` paths in YAML (add `../../` prefix since one level deeper)
- Update footer source links similarly
- Update `related_cards` refs across ALL Elements from `interventions_*` → `ai_interventions_*`
- Update `_INDEX_interventions.md` link paths to point into subfolders

### Partial state from aborted attempt:
- `ai_augmented/` and `taxonomy/` subfolders currently exist with copied files
- Original files still in `cards/` root (not deleted)
- Cross-references NOT yet updated
- **Safe to delete** the `ai_augmented/` and `taxonomy/` folders and start fresh, OR complete the move

---

## 2. Delete Superseded Index Files

These old narrow-scope indices have been replaced by new broader ones:
- `Elements/3_Tools/resources/cards/_INDEX_failure_modes.md` → superseded by `_INDEX_tools.md`
- `Elements/6_Behaviours/resources/cards/_INDEX_verification.md` → superseded by `_INDEX_behaviours.md`

---

## 3. Post-Workshop Refinement (After Delivery)
- Review which cards were actually grabbed during live facilitation
- Merge cards that were always used together
- Split any that proved too broad
- Adjust metadata based on real usage patterns
